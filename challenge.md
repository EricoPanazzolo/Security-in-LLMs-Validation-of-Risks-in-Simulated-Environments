## 🚀 Instructions

### 1. Build the container

```bash
docker build -t llm-ctf-excessive-agency .
```

### 2. Run the container (with log sharing enabled)

```bash
docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name LLM06 llm-ctf-excessive-agency
```

### 3. Access the challenge

```bash
http://localhost:5000
```

### 4. Access the database to verify the deletion/update

Inside the container, you can access the database using the following command:

```bash
sqlite3 /app/client_data.db
```

### 5. Check the contents of the database

```sql
SELECT * FROM employees;
```
