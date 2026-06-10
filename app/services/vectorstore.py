import chromadb

client = chromadb.PersistentClient(
    path="./app/db/chroma_db"
)

collection = client.get_or_create_collection(
    name="current_affairs"
)