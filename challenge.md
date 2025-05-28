# LLM05:2025 Improper Output Handling

## 🚀 Instructions

### 1. Enter in the application directory

```bash
cd llm05-improper-output-handling
```

### 2. Build the container

```bash
docker build -t llm-ctf-improper-output-handling .
```

### 3. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM05 llm-ctf-improper-output-handling
```

### 4. Access in the browser

```bash
http://localhost:5000
```
