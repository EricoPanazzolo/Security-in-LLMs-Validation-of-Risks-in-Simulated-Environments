FROM python:3.9-slim

WORKDIR /app

# Update system packages
RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY app/llm01_app.py .
COPY app/llm01_defense.py .
COPY app/prompts.txt .
COPY app/templates/ ./templates/
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a shared directory for logs and CSV outputs
RUN mkdir -p /app/shared

# Set Flask environment variables
ENV FLASK_APP=llm01_app.py
# ENV FLASK_APP=llm01_defense.py
ENV FLASK_ENV=production

# Expose port for the Flask application
EXPOSE 5000

# Launch the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]
