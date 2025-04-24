# Base da imagem com Python
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

# Cria diretório compartilhado para logs e CSV
RUN mkdir -p /app/shared

# Variáveis de ambiente do Flask
ENV FLASK_APP=llm05_app.py
ENV FLASK_ENV=production

# Expondo porta padrão do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
