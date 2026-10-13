
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


texts = [
    """If you're developing an application, you'll want to make sure
    you're testing it under conditions that closely simulate a production
    environment. Production users generate large volumes of varied data,
    which helps expose bugs that manual testing may miss.""",

    "Python is a programming language.",
    "Streamlit is used to build web apps.",
    "Dogs are friendly animals.",
    "Cats like to sleep a lot."
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_texts(texts, embeddings)

vector_store.save_local("vector_store")

print("All texts are stored in the vector store!")

vector_store = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Madhan Prakash vector store is ready!")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

print("Retriever is ready!")

question = "What is used to build web apps?"

results = retriever.invoke(question)

print("Question:", question)
print("\nRelevant information found:")

for r in results:
    print("-", r.page_content)
