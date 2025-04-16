# LLM02: Sensitive Information Disclosure

## Objective

Try to extract sensitive information of a language model.

## Instructions

1. Build the container: `docker build -t llm-ctf-sensitive-info-disc .`
2. Run this command to shared the files: `docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name llm_ctf-02 llm-ctf-sensitive-info-disc`
3. Access the challenge in your browser: `http://localhost:5000`
