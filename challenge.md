# LLM03:2025 Supply Chain, LLM04:2025 Data and Model Poisoining e LLM08:2025 Vector and Embedding Weakenesses

## 🚀 Instructions

### 1. Enter in the application directory

```bash
cd llm03-04-08-sc-dmp-vew
```

### 2. Build the container

```bash
docker build -t llm-ctf-sc-dmp-vew .
```

### 3. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM03-04-08 llm-ctf-sc-dmp-vew
```

### 4. Access in the browser

```bash
http://localhost:5000
```
