# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port (8003)
EXPOSE 8003

# Run FastAPI with Uvicorn on port 8003
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
