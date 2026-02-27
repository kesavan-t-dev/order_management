# Use a lightweight Python base image
FROM python:3.13.11-slim

# Ensure logs are flushed immediately
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency files first (for caching)
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Default command to run FastAPI
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
