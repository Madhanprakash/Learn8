import os

# Turn LangSmith tracking ON
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "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"   # <-- paste your key
os.environ["LANGSMITH_PROJECT"] = "week2project"          # runs are grouped under this name
os.environ["OPENAI_API_KEY"] = "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"          # <-- paste your key

print("LangSmith is connected!")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
prompts = ["live", "breathe", "love"]
#prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")

for p in prompts:
    print(llm.invoke(p).content)