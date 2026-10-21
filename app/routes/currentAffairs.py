from fastapi import APIRouter
# from app.services.newsfetcher import newsfetcher
# from app.services.ingestion import ingest_articles

# from app.schemas.query import QueryRequest
# from app.services.retrieval import retrieve_context
# from app.services.rag import answer_question
from app.services.topic_curator import curate_topics
from app.schemas.news import CountryRequest
from app.services.newsfetcher import newsfetcher as fetch_country_news

router = APIRouter(
    prefix="/current-affairs",
    tags=["Current Affairs"]
)
api_router = APIRouter(tags=["Current Affairs"])


# @router.get("/news")
# def get_news():

#     articles = newsfetcher()

#     return {
#         "count": len(articles),
#         "articles": articles
#     }

# @router.post("/ingest")
# def ingest_news():

#     articles = newsfetcher()

#     count = ingest_articles(articles)

#     return {
#         "chunks_stored": count
#     }

# @router.post("/search")
# def search_news(data: QueryRequest):

#     documents = retrieve_context(
#         data.question
#     )

#     return {
#         "question": data.question,
#         "context": documents
#     }

# @router.post("/ask")
# def ask_question(data: QueryRequest):

#     return answer_question(
#         data.question
#     )



def _get_trending_news(country: str):
    articles = fetch_country_news(
        country
    )

    curated_topics = curate_topics(
        articles
    )

    return curated_topics


@router.get("/trending")
def trending_news(country: str):
    return _get_trending_news(country)


@router.post("/trending")
def trending_news_for_country(data: CountryRequest):
    return _get_trending_news(data.country)


@api_router.post("/api/current-events")
def current_events(country: str):
    return _get_trending_news(country)