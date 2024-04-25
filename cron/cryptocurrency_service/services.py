import aiohttp


async def fetch_crypto_data():
    """
    Fetch cryptocurrency data from the CoinMarketCap API.
    """
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "100",
        "convert": "USD",
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "e9b30c13-9034-4b17-bf2d-7b28a3bed7ea",
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=parameters, headers=headers) as response:
                data = await response.json()
                return data["data"]  # Extracting the cryptocurrency data
        except aiohttp.ClientError as e:
            print(f"Error fetching cryptocurrency data: {e}")
            return None


async def store_crypto_data(crypto_data, pool):
    """
    Store cryptocurrency data into the database.
    """
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("USE crypto_db")
            # Insert each cryptocurrency's data into the table
            for crypto in crypto_data:
                name = crypto["name"]
                symbol = crypto["symbol"]
                price = crypto["quote"]["USD"]["price"]
                await cursor.execute(
                    "INSERT INTO crypto_price (name, symbol, price) VALUES (%s, %s, %s)",
                    (name, symbol, price),
                )
