# agent_utils.py
import os
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

# Set your API keys
os.environ["GROQ_API_KEY"] = "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"
TAVILY_API_KEY = "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"

# Define and export the agent
agent = Agent(
    "groq:llama-3.1-8b-instant",
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results.",
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    return result.output
