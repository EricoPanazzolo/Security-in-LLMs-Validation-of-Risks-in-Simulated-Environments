# LLM05:2025 Improper Output Handling

## 🚀 Instructions

### 1. Enter in the application directory

```bash
cd llm05-improper-output-handling
```

### 2. Choose the defense mode or the attack mode:

- **Defense Mode**: The application has a mitigation strategy in place.
- **Attack Mode**: The application is vulnerable.

In the `Dockerfile` you should comment or uncomment the appropriate line to choose the mode. The following lines are an example of the defense mode active:

```dockerfile
# ENV FLASK_APP=llm05_app.py
ENV FLASK_APP=llm05_defense.py
```

### 3. Build the container

```bash
docker build -t llm-ctf-improper-output-handling .
```

### 4. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM05 llm-ctf-improper-output-handling
```

### 5. Access in the browser

```bash
http://localhost:5000
```
