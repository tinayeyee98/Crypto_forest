from pydantic import BaseModel


class CryptocurrencyPrices(BaseModel):
    name: str
    symbol: str
    price: float
