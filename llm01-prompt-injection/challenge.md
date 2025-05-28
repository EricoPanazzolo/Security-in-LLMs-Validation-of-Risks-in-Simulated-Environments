# LLM01:2025 Prompt Injection

## 🚀 Instructions

### 1. Build the container

`docker build -t llm-ctf-prompt-injection .`

### 2. Run the container (with log sharing enabled)

`docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM01 llm-ctf-prompt-injection`

### 3. Access in the browser

`http://localhost:5000`
