import asyncio
import logging
from datetime import datetime

import aiomysql

from cron.cryptocurrency_service import services


async def create_or_update_db(pool):
    """
    Create the database if it doesn't exist or update it if it exists.
    """
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("CREATE DATABASE IF NOT EXISTS crypto_db")
            await cursor.execute("USE crypto_db")
            await cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS crypto_price (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    symbol VARCHAR(255),
                    price FLOAT
                )
            """
            )


async def run_job(pool):
    """
    Run the job to fetch and store cryptocurrency data.
    """
    start_time = datetime.now()
    await create_or_update_db(pool)
    crypto_data = await services.fetch_crypto_data()
    if crypto_data:
        await services.store_crypto_data(crypto_data, pool)
    end_time = datetime.now()
    execution_time = (end_time - start_time).total_seconds()
    logging.info(f"Job executed in {execution_time} seconds.")


async def main():
    """
    Main entry point of the job service.
    """
    logging.basicConfig(level=logging.INFO)

    # Connect to the MySQL database
    pool = await aiomysql.create_pool(
        host="localhost", user="root", password="root", autocommit=True
    )

    # Run the job
    await run_job(pool)


if __name__ == "__main__":
    asyncio.run(main())
