from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_texts(texts, embeddings)

print("Madhan prakash vector store is ready!")