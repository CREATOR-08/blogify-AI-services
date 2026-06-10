from app.services.embeddings import generate_embedding
from app.services.vectorstore import collection


def retrieve_context(question: str, n_results: int = 5):

    query_embedding = generate_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    documents = results["documents"][0]

    return documents