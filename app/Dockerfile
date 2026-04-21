# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app.py .

# Expose application port
EXPOSE 5000

# Run as non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Start the application
CMD ["python", "app.py"]
