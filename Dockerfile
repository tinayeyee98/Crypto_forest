# Use the official python3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy application into the container
COPY . .

# Create a virtual environment
RUN python -m venv .venv

# Activate the virtual environment
ENV PATH="./app/.venv/bin:$PATH"

# Upgrade pip in the virtual environment
RUN pip install --no-cache-dir --upgrade pip

# Install the required python packages
RUN pip install -r requirements.txt

# Expose the port on which FastAPI will run
EXPOSE 8000

# Serve application with uvicorn server.
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
