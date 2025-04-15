# LLM01: Prompt Injection Challenge

## Objective

Exploit the prompt injection vulnerability to make the LLM reveal its system prompt or perform unintended actions.

## Instructions

1. Build the container: `docker build -t llm-ctf-prompt-injection .`
<!-- 2. Run the container: `docker run -p 5000:5000 llm-ctf-prompt-injection` -->
2. Run this command to shared the files: `docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name llm_ctf llm-ctf-prompt-injection`
3. Access the challenge in your browser: `http://localhost:5000`
4. Find the flag in the system prompt.
