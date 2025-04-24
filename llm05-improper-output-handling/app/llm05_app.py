from flask import Flask, render_template, request, jsonify, make_response
from markupsafe import Markup
from openai import OpenAI
import logging
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Diretório compartilhado
shared_dir = '/app/shared'
os.makedirs(shared_dir, exist_ok=True)

# Arquivos de log e CSV
log_file = os.path.join(shared_dir, "app.log")
csv_filename = os.path.join(
    shared_dir,
    f"llm05_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
)

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
)

# Cliente HF via OpenAI-compatible inference endpoint
HF_TOKEN     = os.environ.get("HF_TOKEN", "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")
ENDPOINT_URL = "https://xi7atce6p426bl0y.us-east-1.aws.endpoints.huggingface.cloud/v1/"
MODEL_NAME   = "mistralai/Mistral-7B-Instruct-v0.1"

client = OpenAI(base_url=ENDPOINT_URL, api_key=HF_TOKEN)

# Cria CSV com cabeçalho
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Prompt', 'Response', 'Effective'])

@app.route('/')
def home():
    # Gera a página inicial e define um cookie de sessão 'session_id'
    resp = make_response(render_template('llm05_challenge.html'))
    resp.set_cookie('session_id', 'PUCRS_COOKIE_SESSION_123', path='/', httponly=False)  # Sem HttpOnly para XSS demo
    return resp

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get("message", "").strip()
    logging.info(f"Prompt recebido: {prompt}")
    if not prompt:
        return jsonify({'error': 'No message provided'}), 400

    result = handle_prompt(prompt)
    return jsonify(result)

def handle_prompt(prompt):
    try:
        SYSTEM_PROMPT = "Você é um assistente que responde em HTML/Markdown."
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=200
        )

        reply = completion.choices[0].message.content.strip()
        effective = prompt in reply

        logging.info(f"Resposta do modelo: {reply}")
        if effective:
            logging.warning("⚠️ Ataque XSS efetivo detectado!")

        # Grava no CSV
        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                prompt,
                reply,
                'Yes' if effective else 'No'
            ])

        return {'response': reply, 'effective': effective}

    except Exception as e:
        logging.error(f"Erro ao processar prompt: {e}")
        return {'error': str(e)}

@app.route('/auto-test', methods=['GET'])
def auto_test():
    results = []
    try:
        # Lê prompts de app/prompts.txt
        with open('app/prompts.txt', 'r', encoding='utf-8') as f:
            prompts = [l.strip() for l in f if l.strip()]

        for p in prompts:
            res = handle_prompt(p)
            results.append({'prompt': p, **res})

        return jsonify(results)

    except Exception as e:
        logging.error(f"Erro no auto-teste: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
