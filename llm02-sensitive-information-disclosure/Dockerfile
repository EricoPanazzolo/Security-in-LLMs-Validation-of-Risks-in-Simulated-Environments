# Use uma imagem leve do Python
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY app/llm02_app.py .
COPY app/llm02_app_defense.py .
COPY app/init_db.py .
COPY app/client_data.db .
COPY app/prompts.txt .
COPY app/templates/ ./templates/
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Executa o script de criação do banco (se quiser gerar automaticamente na build)
RUN python init_db.py

# Diretório compartilhado para logs
RUN mkdir -p /app/shared

# Variáveis de ambiente
# ENV FLASK_APP=llm02_app.py
ENV FLASK_APP=llm02_app_defense.py
ENV FLASK_ENV=production

# Expondo a porta padrão do Flask
EXPOSE 5000

# Comando para rodar o servidor
CMD ["flask", "run", "--host=0.0.0.0"]
