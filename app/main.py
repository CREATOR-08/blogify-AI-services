from fastapi import FastAPI
from pydantic import BaseModel

from app.routes import currentAffairs
from app.schemas.tagschema import BlogRequest

from app.routes.tagging import generate_tags
from app.routes.currentAffairs import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js local
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate-tags")
async def handle_generate_tags(request: BlogRequest):
    return await generate_tags(request)


app.include_router(router)