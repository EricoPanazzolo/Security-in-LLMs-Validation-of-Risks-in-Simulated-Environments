## 🚀 Instructions

### 1. Build the container

```bash
docker build -t llm-ctf-unbounded-consumption .
```

### 2. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM10 llm-ctf-unbounded-consumption
```

### 3. Access the challenge

```bash
http://localhost:5000
```
