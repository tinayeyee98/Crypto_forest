FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy application into the container
COPY . /app/cron/cryptocurrency_service

# Create a virtual environment
RUN python -m venv .venv

# Install dependencies
RUN pip install --no-cache-dir aiomysql aiohttp

# Run the script
CMD ["python", "-m", "cron.cryptocurrency_service.main"]
