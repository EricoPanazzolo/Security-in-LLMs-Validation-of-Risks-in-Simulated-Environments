FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY app/llm09_app.py .
COPY app/defense.py .
COPY app/prompts.txt .
COPY app/templates/ ./templates/
COPY requirements.txt .

# Install Python dependencies and initialize the SQLite database
RUN pip install --no-cache-dir -r requirements.txt

# Create a shared directory for logs and CSV outputs
RUN mkdir -p /app/shared

# Set Flask environment variables
ENV FLASK_APP=llm09_app.py
# ENV FLASK_APP=defense.py
ENV FLASK_ENV=production

# Expose port for the Flask application
EXPOSE 5000

# Launch the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]