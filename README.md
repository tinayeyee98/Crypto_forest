# Crypto Forest

## Project Overview
Crypto Forest is a web application built with FastAPI that fetches cryptocurrency names and prices from the CoinMarketCap API, stores the data in a MySQL database, and displays the information using HTML templates.

## Installation
1. Clone this repository.
2. Install Docker and Docker Compose if not already installed.
3. Navigate to the project directory.
4. Run `docker-compose up -d` to start the application.
5. Run `docker build -t cryptocurrency_service .` to start the fetching cryptocurrencies script. Note: you need to navigate to Dockerfile first.

## Usage
- Access the FastAPI documentation at `http://localhost:8000/docs` for API endpoints documentation.
- Visit `http://localhost:8000` to view the homepage.
- Cryptocurrency names and prices are displayed on the homepage.

## Project Structure
- `app/`: Contains the main application code.
    - `database/`: DB connection.
    - `models/`: Data schema models.
    - `routes/`: API route handlers.
    - `services/`: repositories layer for route.
    - `templates/`: HTML templates.
    - `main.py`: Entry point of the FastAPI application.
- `cron/`: Contains cron job services.
- `tests/`: Contains unit testing for the application.
- `docker-compose.yml`: Docker Compose configuration.
- `requirements.txt`: Python dependencies.

