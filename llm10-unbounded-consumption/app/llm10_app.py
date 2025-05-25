from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import logging
import csv
from datetime import datetime
import os

app = Flask(__name__)

# Diretório compartilhado para logs e arquivos CSV
shared_dir = '/app/shared'
os.makedirs(shared_dir, exist_ok=True)

# Configuração de logging
log_file = os.path.join(shared_dir, "llm09_app.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Arquivo CSV com log de respostas
csv_filename = os.path.join(shared_dir, f"llm09_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'User Prompt', 'Model Response', 'Misinformation'])

# Cliente OpenAI com endpoint da Hugging Face
HF_TOKEN = "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"
ENDPOINT_URL = "https://xi7atce6p426bl0y.us-east-1.aws.endpoints.huggingface.cloud/v1/"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

client = OpenAI(
    base_url=ENDPOINT_URL,
    api_key=HF_TOKEN
)

SYSTEM_PROMPT = """
    - You are a friendly, concise chatbot.
    - Always wait for user input before providing additional commentary.
    - When uncertain, ask clarifying questions instead of making assumptions.
"""

@app.route('/')
def home():
    return render_template('llm10_challenge.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')

    logging.info(f"Prompt recebido: {user_message}")

    if not user_message:
        logging.warning("Nenhuma mensagem fornecida.")
        return jsonify({'error': 'No message provided'}), 400

    response_data = handle_prompt(user_message)
    return jsonify(response_data)

def handle_prompt(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            stream=False
        )

        assistant_reply = chat_completion.choices[0].message.content
        
        logging.info(f"Resposta do modelo: {assistant_reply}")

        return {'response': assistant_reply}

    except Exception as e:
        logging.error(f"Erro ao processar a solicitação: {e}")
        return {'error': str(e)}

@app.route('/auto-test', methods=['GET'])
def auto_test():
    test_file = 'prompts.txt'
    results = []

    try:
        with open(test_file, 'r', encoding='utf-8') as file:
            prompts = file.readlines()

        for prompt in prompts:
            prompt = prompt.strip()
            if prompt:
                response_data = handle_prompt(prompt)
                results.append({'prompt': prompt, 'response': response_data})

        return jsonify(results)

    except Exception as e:
        logging.error(f"Erro ao executar auto-teste: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)