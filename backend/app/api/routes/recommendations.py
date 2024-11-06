from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.content_suggestions import generate_suggestions
from app.utils.seo_suggestions import generate_seo_keywords

recommendations_router = APIRouter()

class ContentRequest(BaseModel):
    content: str

@recommendations_router.post("/content")
async def content_suggestions(request: ContentRequest):
    suggestions = generate_suggestions(request.content)
    return {"suggestions": suggestions}

@recommendations_router.get("/seo")
async def seo_recommendations():
    keywords = generate_seo_keywords()
    return {"keywords": keywords}
