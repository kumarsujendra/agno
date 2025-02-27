from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
# from agno.storage.agent.sqlite import SqlAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.tools.googlesearch import GoogleSearchTools

# import json
# import httpx
# from youtube_search import YoutubeSearch

from math_toolkit import MathToolKit
from search_toolkit import SearchToolKit

agent = Agent(
    name="Search Agent",
    agent_id="search_agent",
    role="Search youtube Videos, Maths operations",
    tools=[MathToolKit()],
    show_tool_calls=True, 
    debug_mode=True,
    markdown=True)

# agent.print_response("sum of 2 and 5", stream=True)
app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("agent:app", reload=True)
 