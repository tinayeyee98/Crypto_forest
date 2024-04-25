from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database.db import DatabaseManager
from app.services.crypto import get_cryptocurrency_prices

router = APIRouter(prefix="/v1")
templates = Jinja2Templates(directory="app/templates")
db_manager = DatabaseManager()


@router.get("/cryptocurrencies", response_class=HTMLResponse)
async def get_cryptocurrency_list(request: Request):
    """
    Endpoint to fetch and display a list of cryptocurrencies.

    Args:
        request (Request): The incoming request.

    Returns:
        TemplateResponse: HTML page displaying the list of cryptocurrencies.
    """
    data = await get_cryptocurrency_prices(db_manager)

    return templates.TemplateResponse(request, "index.html", {"data": data})
