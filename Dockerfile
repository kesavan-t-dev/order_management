# Use a lightweight Python base image
FROM python:3.13-slim

# Ensure logs are flushed immediately
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    freetds-dev \
    freetds-bin \
    gcc \
    && rm -rf /var/lib/apt/lists/*


# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency files first
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry lock && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Change host to 0.0.0.0 so it is accessible outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]