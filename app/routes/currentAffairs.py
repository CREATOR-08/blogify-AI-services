from fastapi import APIRouter
from app.services.newsfetcher import newsfetcher
from app.services.ingestion import ingest_articles

from app.schemas.query import QueryRequest
from app.services.retrieval import retrieve_context
from app.services.rag import answer_question
router = APIRouter(
    prefix="/current-affairs",
    tags=["Current Affairs"]
)


# @router.get("/news")
# def get_news():

#     articles = newsfetcher()

#     return {
#         "count": len(articles),
#         "articles": articles
#     }

@router.post("/ingest")
def ingest_news():

    articles = newsfetcher()

    count = ingest_articles(articles)

    return {
        "chunks_stored": count
    }

@router.post("/search")
def search_news(data: QueryRequest):

    documents = retrieve_context(
        data.question
    )

    return {
        "question": data.question,
        "context": documents
    }

@router.post("/ask")
def ask_question(data: QueryRequest):

    return answer_question(
        data.question
    )