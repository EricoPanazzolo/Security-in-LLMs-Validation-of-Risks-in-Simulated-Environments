# LLM02:2025 Sensitive Information Disclosure

## 🚀 Instructions

### 1. Enter in the application directory

```bash
cd llm02-sensitive-information-disclosure
```

### 2. Build the container

```bash
docker build -t llm-ctf-sensitive-information-disclosure .
```

### 3. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM02 llm-ctf-sensitive-information-disclosure
```

### 4. Access in the browser

```bash
http://localhost:5000
```
