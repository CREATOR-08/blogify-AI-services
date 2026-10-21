
from app.schemas.tagschema import BlogRequest
from dotenv import load_dotenv
from google import genai
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = os.getenv("GEMINI_MODEL")


async def generate_tags(data: BlogRequest):
    prompt = f"""
    Generate 5 relevant blog tags based on title and content.

    Return ONLY valid JSON in this format:
    {{
      "tags": ["AI", "LIFESTYLE", "TECHNOLOGY", "FUTURE", "INNOVATION"]
    }}

    Title:
    {data.title}

    Content:
    {data.content}
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    result = json.loads(response.text)
    return result
