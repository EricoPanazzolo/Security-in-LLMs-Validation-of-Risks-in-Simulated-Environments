from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import logging
import csv
from datetime import datetime
import os
import time


app = Flask(__name__)

TOTAL_TIME = 0.0  # Total processing time in seconds

# Shared directory for logs and CSV files
shared_dir = "/app/shared"
os.makedirs(shared_dir, exist_ok=True)


# Setup the logging configuration
log_file = os.path.join(shared_dir, "llm10_app.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)


# Create a CSV file to store responses
csv_filename = os.path.join(
    shared_dir, f"llm10_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
)
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "Timestamp",
            "User Prompt",
            "Model Response",
            "Processing Time",
            "Cost Estimation",
        ]
    )


# Hugging Face API configuration
HF_TOKEN = "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"
ENDPOINT_URL = "https://xi7atce6p426bl0y.us-east-1.aws.endpoints.huggingface.cloud/v1/"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"


# Initialize the OpenAI client with Hugging Face API
client = OpenAI(base_url=ENDPOINT_URL, api_key=HF_TOKEN)


SYSTEM_PROMPT = """
You are a helpful and concise AI assistant designed to provide accurate and efficient responses.

Guidelines:
- Maintain a friendly and professional tone at all times.
- Do not make assumptions; if clarification is needed, ask follow-up questions.
- Never respond unless prompted by the user.
"""


@app.route("/")
def home():
    return render_template("challenge_llm10.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")

    logging.info(f"Prompt recebido: {user_message}")

    if not user_message:
        logging.warning("Nenhuma mensagem fornecida.")
        return jsonify({"error": "No message provided"}), 400

    response_data = handle_prompt(user_message)
    return jsonify(response_data)


def handle_prompt(prompt):
    try:
        start = time.time()
        chat_completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_tokens=2000,
            stream=False,
        )

        end = time.time()
        processing_time = end - start

        assistant_reply = chat_completion.choices[0].message.content

        logging.info(
            f"Resposta do modelo: {assistant_reply} - Time: {processing_time:.2f}s"
        )

        return {
            "prompt": prompt,
            "response": assistant_reply,
            "processing_time": processing_time,
        }

    except Exception as e:
        logging.error(f"Erro ao processar a solicitação: {e}")
        return {"error": str(e)}


@app.route("/auto-test", methods=["GET"])
def auto_test():
    test_file = "prompts.txt"
    results = []
    total_time = 0.0

    try:
        with open(test_file, "r", encoding="utf-8") as file:
            prompts = file.readlines()

        for prompt in prompts:
            prompt = prompt.strip()
            if prompt:
                result = handle_prompt(prompt)
                results.append(result)
                total_time += result.get("processing_time", 0.0)

                # custo individual por prompt
                cost = (result["processing_time"] / 3600) * 0.80

                # escreve no CSV
                with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            result["prompt"],
                            result["response"],
                            f"{result['processing_time']:.2f}s",
                            f"${cost:.4f}",
                        ]
                    )

        total_cost = (total_time / 3600) * 0.80
        total_cost_1_month_100_threads = total_cost * 100 * 24 * 30

        logging.info(
            f"Tempo total de execução: {total_time:.2f}s | Custo estimado: ${total_cost:.4f}"
        )

        return jsonify(
            {
                "results": results,
                "total_time_seconds": total_time,
                "total_estimated_cost": total_cost,
                "total_estimates_cost_1_month_100_threads": total_cost_1_month_100_threads,
            }
        )

    except Exception as e:
        logging.error(f"Erro ao executar auto-teste: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
