import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def newsfetcher():


    url = (
    f"https://newsapi.org/v2/everything"
    f"?q=(India OR Pakistan OR China OR USA OR Technology OR AI OR Economy OR Politics)"
    f"&sortBy=publishedAt"
    f"&pageSize=10"
    f"&apiKey={NEWS_API_KEY}"
)

    response = requests.get(url)

    print("STATUS:", response.status_code)
    print("DATA:", response.json())

    return response.json().get("articles", [])