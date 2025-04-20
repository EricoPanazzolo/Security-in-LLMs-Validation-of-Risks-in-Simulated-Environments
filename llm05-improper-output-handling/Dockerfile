# Imagem base do Python
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY app/llm05_app.py .
COPY app/prompts.txt .
COPY app/templates/ ./templates/
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Cria o diretório compartilhado para logs
RUN mkdir -p /app/shared

# Variáveis de ambiente do Flask
ENV FLASK_APP=llm05_app.py
ENV FLASK_ENV=production

# Exposição da porta padrão
EXPOSE 5000

# Comando de inicialização
CMD ["flask", "run", "--host=0.0.0.0"]
