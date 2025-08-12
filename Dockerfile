# Use an official Python runtime
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Command to run app
CMD ["python", "app.py"]
