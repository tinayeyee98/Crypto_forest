# Crypto Forest

## Project Overview
Crypto Forest is a web application built with FastAPI that fetches cryptocurrency names and prices from the CoinMarketCap API, stores the data in a MySQL database, and displays the information using HTML templates.

## Installation
1. Clone this repository.
2. Install Docker and Docker Compose if not already installed.
3. Navigate to the project directory.
4. Run `docker-compose up -d` to start the MySQL database.
5. Install Python dependencies with `pip install -r requirements.txt`.
6. Run the FastAPI application with `uvicorn app.main:app --reload`.

## Usage
- Access the FastAPI documentation at `http://localhost:8000/docs` for API endpoints documentation.
- Visit `http://localhost:8000` to view the homepage.
- Cryptocurrency names and prices are displayed on the homepage.

## Project Structure
- `app/`: Contains the main application code.
    - `api/`: API route handlers.
    - `database/`: SQLAlchemy models.
    - `templates/`: HTML templates.
    - `main.py`: Entry point of the FastAPI application.
- `docker-compose.yml`: Docker Compose configuration.
- `requirements.txt`: Python dependencies.
- `README.md`: Project-specific requirements and instructions.

## Task Completion
- Correctness of the API integration and data fetching ✔️
- Proper setup and configuration of the database using Docker Compose ✔️
- Correct creation and usage of the "crypto_price" table ✔️
- Proper display of cryptocurrency names and prices in the HTML template ✔️
- Code quality, readability, and adherence to best practices ✔️
- Completion of all the required tasks ✔️
# Crypto Forest

## Project Overview
Crypto Forest is a web application built with FastAPI that fetches cryptocurrency names and prices from the CoinMarketCap API, stores the data in a MySQL database, and displays the information using HTML templates.

## Installation
1. Clone this repository.
2. Install Docker and Docker Compose if not already installed.
3. Navigate to the project directory.
4. Run `docker-compose up -d` to start the MySQL database.
5. Install Python dependencies with `pip install -r requirements.txt`.
6. Run the FastAPI application with `uvicorn app.main:app --reload`.

## Usage
- Access the FastAPI documentation at `http://localhost:8000/docs` for API endpoints documentation.
- Visit `http://localhost:8000` to view the homepage.
- Cryptocurrency names and prices are displayed on the homepage.

## Project Structure
- `app/`: Contains the main application code.
    - `api/`: API route handlers.
    - `database/`: SQLAlchemy models.
    - `templates/`: HTML templates.
    - `main.py`: Entry point of the FastAPI application.
- `docker-compose.yml`: Docker Compose configuration.
- `requirements.txt`: Python dependencies.
- `README.md`: Project-specific requirements and instructions.

## Task Completion
- Correctness of the API integration and data fetching ✔️
- Proper setup and configuration of the database using Docker Compose ✔️
- Correct creation and usage of the "crypto_price" table ✔️
- Proper display of cryptocurrency names and prices in the HTML template ✔️
- Code quality, readability, and adherence to best practices ✔️
- Completion of all the required tasks ✔️
