from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.db import DatabaseManager
from app.routes.v1 import crypto_api

app = FastAPI()

# Mounting static files directory for templates
app.mount("/static", StaticFiles(directory="app/templates"), name="static")

# Update the database connection parameters here
db_manager = DatabaseManager(host="db", user="root", password="root", db="crypto_db")

# Including routers
app.include_router(crypto_api.router)
