# LLM01:2025 Prompt Injection

## 🚀 Instructions

### 1. Enter in the application directory

```bash
cd llm01-prompt-injection
```

### 2. Choose the defense mode or the attack mode:

- **Defense Mode**: The application has a mitigation strategy in place.
- **Attack Mode**: The application is vulnerable.

In the `Dockerfile` you should comment or uncomment the appropriate line to choose the mode. The following lines are an example of the defense mode active:

```dockerfile
# ENV FLASK_APP=llm01_app.py
ENV FLASK_APP=llm01_defense.py
```

### 3. Build the container

```bash
docker build -t llm-ctf-prompt-injection .
```

### 4. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM01 llm-ctf-prompt-injection
```

### 5. Access in the browser

```bash
http://localhost:5000
```
