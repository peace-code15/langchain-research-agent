from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain.agents import create_react_agent
from tools import web_search, scrape_article

tools = [
    Tool(
        name="Web Search",
        func=web_search,
        description="Search the internet for information about a topic"
    ),
    Tool(
        name="Web Scraper",
        func=scrape_article,
        description="Scrape content from a URL. Input must be a valid URL."
    ),
]

llm = ChatOllama(model="llama3.1")  # use llama3.1, not mistral

agent_executor = create_react_agent(llm, tools)

def run_agent(query: str):
    result = agent_executor.invoke({"messages": [("human", query)]})
    return result["messages"][-1].content