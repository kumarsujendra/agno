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

web_search_agent = Agent(
    name="Web Search Agent",
    agent_id="weg_search_agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    storage=SqliteAgentStorage(table_name="web_search_agent_session", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)


video_search_agent = Agent(
    name="Video Search Agent",
    agent_id="video_search_agent",
    role="Search the video for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Search videos on youtube only"],
    storage=SqliteAgentStorage(table_name="video_search_agent_session", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

team_agent = Agent(
    name="Team Agent",
    agent_id="team_agent",
    team=[web_search_agent, video_search_agent],
    storage=SqliteAgentStorage(table_name="team_agent_session", db_file="agents.db"),
    markdown=True,
)

app = Playground(agents=[web_search_agent, video_search_agent, team_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("search2:app", reload=True)
 