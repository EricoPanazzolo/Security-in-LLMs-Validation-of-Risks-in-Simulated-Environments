# LLM01:2025 Prompt Injection

## 🚀 Instructions

### 1. Enter in the application directory

```bash
cd llm01-prompt-injection
```

### 2. Build the container

```bash
docker build -t llm-ctf-prompt-injection .
```

### 3. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM01 llm-ctf-prompt-injection
```

### 4. Access in the browser

```bash
http://localhost:5000
```
