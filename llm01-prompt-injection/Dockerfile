# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the required files
COPY ctf_app.py .
COPY ctf_app_defense.py .
COPY prompts.txt .
COPY requirements.txt .
COPY templates/ ./templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Environment variables
ENV FLASK_APP=ctf_app_defense.py
# ENV FLASK_APP=ctf_app.py
ENV FLASK_ENV=production

# Expose port 5000 (Flask default)
EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
