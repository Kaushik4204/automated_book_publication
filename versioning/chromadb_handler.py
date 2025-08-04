import chromadb

def store_version(content, metadata):
    client = chromadb.Client()
    collection = client.get_or_create_collection("book_versions")
    collection.add(
        documents=[content],
        metadatas=[metadata],
        ids=[metadata["id"]]
    )

def semantic_search(query):
    client = chromadb.Client()
    collection = client.get_or_create_collection("book_versions")
    results = collection.query(query_texts=[query], n_results=3)
    return results
