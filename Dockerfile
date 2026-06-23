# Use lightweight python base image
FROM python:3.11-slim

# Prevent python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /workspace

# Install system build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . /workspace/

# Expose port for FastAPI application
EXPOSE 9101

# Default command to run the FastAPI app (can be overridden for Celery worker role)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9101"]
