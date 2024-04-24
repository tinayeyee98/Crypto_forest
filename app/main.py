import json
from pathlib import Path

import fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from app.routes.v1 import crypto_api

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(crypto_api.router)


if __name__ == '__main__':
    configure()