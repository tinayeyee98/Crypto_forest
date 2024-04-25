import asyncio

from fastapi import HTTPException

from app.database.db import DatabaseManager
from app.models.crypto_model import CryptocurrencyPrices


async def get_cryptocurrency_prices(
    db_manager: DatabaseManager,
) -> list[CryptocurrencyPrices]:
    """
    Retrieve the latest cryptocurrency prices from the database.

    Args:
        db_manager (DatabaseManager): An instance of DatabaseManager to execute queries.

    Returns:
        List[CryptocurrencyPrices]: A list of CryptocurrencyPrices objects representing cryptocurrency prices.

    Raises:
        HTTPException: If an error occurs while fetching cryptocurrency prices from the database.
    """
    try:
        # Connect to the database
        await db_manager.connect()

        # Fetch cryptocurrency prices from the database
        data = await db_manager.execute_query(
            "SELECT name, symbol, price FROM crypto_price ORDER BY name ASC"
        )

        if not data:
            # If no records found, raise HTTPException with status code 404
            raise HTTPException(
                status_code=404,
                detail="No data found in the database.",
            )

        # Convert data to list of CryptocurrencyPrices objects
        cryptocurrencies = [
            CryptocurrencyPrices(name=name, symbol=symbol, price=price)
            for name, symbol, price in data
        ]

        return cryptocurrencies

    except Exception as e:
        # Log the error or handle it as needed
        raise HTTPException(
            status_code=500,
            detail="Error fetching cryptocurrency prices from database.",
        )

    finally:
        # Disconnect from the database
        await db_manager.disconnect()
