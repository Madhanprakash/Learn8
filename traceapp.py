import os

# Turn LangSmith tracking ON
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "week2project"          # runs are grouped under this name

print("LangSmith is connected!")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
prompts = ["live", "breathe", "love"]
#prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")

for p in prompts:
    print(llm.invoke(p).content)