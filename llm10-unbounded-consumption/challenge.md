## 🚀 Instructions

### 1. Build the container

`docker build -t llm-ctf-unbounded-consumption .`

### 2. Run the container (with log sharing enabled)

`docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name llm_ctf-10 llm-ctf-unbounded-consumption`

### 3. Access the challenge

`http://localhost:5000`
