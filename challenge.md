## 🚀 Instructions

### 1. Build the container

```bash
docker build -t llm-ctf-excessive-agency .
```

### 2. Choose the defense mode or the attack mode:

- **Defense Mode**: The application has a mitigation strategy in place.
- **Attack Mode**: The application is vulnerable.

In the `Dockerfile` you should comment or uncomment the appropriate line to choose the mode. The following lines are an example of the defense mode active:

```dockerfile
# ENV FLASK_APP=llm06_app.py
ENV FLASK_APP=llm06_defense.py
```

### 3. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM06 llm-ctf-excessive-agency
```

### 4. Access the challenge

```bash
http://localhost:5000
```

### 5. Access the database to verify the deletion/update

Inside the container, you can access the database using the following command:

```bash
sqlite3 /app/client_data.db
```

### 6. Check the contents of the database

```sql
SELECT * FROM employees;
```
