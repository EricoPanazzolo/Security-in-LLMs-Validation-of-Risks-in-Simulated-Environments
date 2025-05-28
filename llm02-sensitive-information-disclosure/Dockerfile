FROM python:3.9-slim

WORKDIR /app

# Base files and directories
COPY app/llm02_app.py .
COPY app/llm02_app_defense.py .
COPY app/init_db.py .
COPY app/client_data.db .
COPY app/prompts.txt .
COPY app/templates/ ./templates/
COPY requirements.txt .

# Install system dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Database initialization
RUN python init_db.py

# Shared directory for logs
RUN mkdir -p /app/shared

# Envonriments variables
# ENV FLASK_APP=llm02_app.py
ENV FLASK_APP=llm02_app_defense.py
ENV FLASK_ENV=production

# Expondo a porta padrão do Flask
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
