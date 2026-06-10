# app/schemas/news.py

from pydantic import BaseModel

class CountryRequest(BaseModel):
    country: str