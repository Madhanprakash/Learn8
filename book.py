from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\MADHAN PRAKASH\Downloads\vel paari.pdf")
pages = loader.load()

print(f"Loaded {len(pages)} pages")

for page in pages[:2]:
    print(page.page_content[:300])