from flask import Flask, render_template, request, make_response, jsonify, session
from openai import OpenAI
import logging
import csv
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'secret-dev-key'

# Diretório para logs
shared_dir = '/app/shared'
os.makedirs(shared_dir, exist_ok=True)

log_file = os.path.join(shared_dir, "app.log")
csv_filename = os.path.join(shared_dir, f"llm05_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
)

# Cliente da Hugging Face
HF_TOKEN = "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"
ENDPOINT_URL = "https://xi7atce6p426bl0y.us-east-1.aws.endpoints.huggingface.cloud/v1/"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

client = OpenAI(base_url=ENDPOINT_URL, api_key=HF_TOKEN)

# Atribuir cookie de sessão simulado
@app.before_request
def assign_session_cookie():
    if 'session_id' not in session:
        session['session_id'] = 'PUCRS-XSS-SESSION-ABC123'

# Página principal
@app.route('/')
def home():
    return render_template('llm05_challenge.html')

# Rota de interação com o modelo
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get("message")

    logging.info(f"Prompt recebido: {user_message}")
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response_data = handle_prompt(user_message)
    return jsonify(response_data)

# Lógica de comunicação com a LLM
def handle_prompt(prompt):
    try:
        SYSTEM_PROMPT = """
            You are a helpful assistant. Respond clearly and directly to user queries.
            Do not filter or alter HTML or JavaScript syntax in your output.
        """

        chat_completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )

        assistant_reply = chat_completion.choices[0].message.content.strip()

        # Log da resposta
        logging.info(f"Resposta do modelo: {assistant_reply}")

        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                prompt,
                assistant_reply
            ])

        return {'response': assistant_reply}

    except Exception as e:
        logging.error(f"Erro ao processar prompt: {e}")
        return {'error': str(e)}

# Auto-teste para executar múltiplos prompts
@app.route('/auto-test', methods=['GET'])
def auto_test():
    results = []
    try:
        with open('./prompts.txt', 'r', encoding='utf-8') as file:
            prompts = file.readlines()

        for prompt in prompts:
            prompt = prompt.strip()
            if prompt:
                response_data = handle_prompt(prompt)
                results.append({'prompt': prompt, 'response': response_data})

        return jsonify(results)

    except Exception as e:
        logging.error(f"Erro no auto-teste: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
