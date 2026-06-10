from app.schemas.tagschema import BlogRequest
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(os.getenv("GEMINI_MODEL"))  

async def generate_tags(data: BlogRequest):

    prompt = f"""
    Generate 5 relevant blog tags based on title and content.

    Return ONLY valid JSON.

    Example:
    {{
      "tags": ["AI","LIFESTYLE","TECHNOLOGY","FUTURE","INNOVATION"]
    }}

    Title:
    {data.title}

    Content:
    {data.content}
    """

    response = model.generate_content(prompt)

    response_text = response.text.strip()

    response_text = (
        response_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    result = json.loads(response_text)

    return result