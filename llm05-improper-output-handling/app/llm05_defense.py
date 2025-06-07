from flask import Flask, render_template, request, jsonify, make_response
from markupsafe import Markup
from openai import OpenAI
import logging
import csv
import os
from datetime import datetime
import bleach

app = Flask(__name__)


# Shared directory for logs and CSV files
shared_dir = "/app/shared"
os.makedirs(shared_dir, exist_ok=True)


# Setup the logging configuration
log_file = os.path.join(shared_dir, "app.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)


# Create a CSV file to store responses
csv_filename = os.path.join(
    shared_dir, f"prompt_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
)
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "User Prompt", "Model Response", "Effective"])


# Initialize the OpenAI client with Hugging Face API
HF_TOKEN     = os.environ.get("HF_TOKEN", "YOUR_TOKEN_GOES_HERE" ) # Replace with your Hugging Face token
ENDPOINT_URL = "YOUR_ENDPOINT_URL_GOES_HERE"  # Replac
MODEL_NAME   = "mistralai/Mistral-7B-Instruct-v0.1"


client = OpenAI(base_url=ENDPOINT_URL, api_key=HF_TOKEN)


@app.route('/')
def home():
    ## Define a session cookie for the user
    resp = make_response(render_template('llm05_challenge.html'))
    resp.set_cookie('session_id', 'PUCRS_COOKIE_SESSION_123', path='/', httponly=False)  # HttpOnly set to False for testing purposes
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

        raw_reply = completion.choices[0].message.content.strip()

        # Sanitize the raw reply to prevent XSS and other issues
        sanitized_reply = bleach.clean(
            raw_reply,
            tags=['b', 'i', 'em', 'strong', 'ul', 'ol', 'li', 'p', 'code', 'pre', 'br'],
            attributes={},
            protocols=['http', 'https'],
            strip=True
        )

        logging.info(f"Resposta do modelo (sanitizada): {sanitized_reply}")

        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                prompt,
                raw_reply,
                sanitized_reply
            ])

        return {'response': sanitized_reply}

    except Exception as e:
        logging.error(f"Erro ao processar prompt: {e}")
        return {'error': str(e)}


@app.route('/auto-test', methods=['GET'])
def auto_test():
    results = []
    try:
        with open('/prompts.txt', 'r', encoding='utf-8') as f:
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
