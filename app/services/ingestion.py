from app.services.chunking import chunk_text
from app.services.embeddings import generate_embedding
from app.services.vectorstore import collection


def ingest_articles(articles):

    total_chunks = 0

    for article in articles:

        content = article.get("content")

        if not content:
            continue

        chunks = chunk_text(content)

        for idx, chunk in enumerate(chunks):

            embedding = generate_embedding(chunk)

            collection.add(
                ids=[
                    f"{article.get('title')}_{idx}"
                ],
                documents=[chunk],
                embeddings=[embedding]
            )

            total_chunks += 1

    return total_chunks