from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
import asyncio

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    agent_id="web_search_agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    storage=SqliteAgentStorage(table_name="web_search_agent_session", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Video Search Agent
video_search_agent = Agent(
    name="Video Search Agent",
    agent_id="video_search_agent",
    role="Search videos on YouTube",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Search videos on YouTube only"],
    storage=SqliteAgentStorage(table_name="video_search_agent_session", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Team Agent for handling multimodal search
async def multimodal_search(query: str):
    # Trigger both web and video search agents in parallel
    web_search_results = await web_search_agent.call(query)
    video_search_results = await video_search_agent.call(query)
    
    # Combine the results (you can customize how you combine them)
    combined_results = {
        "web_results": web_search_results.get("response"),
        "video_results": video_search_results.get("response")
    }

    return combined_results

# Team agent to coordinate between the two search agents
team_agent = Agent(
    name="Team Agent",
    agent_id="team_agent",
    team=[web_search_agent, video_search_agent],
    storage=SqliteAgentStorage(table_name="team_agent_session", db_file="agents.db"),
    markdown=True,
)

# Playground app setup
app = Playground(agents=[web_search_agent, video_search_agent, team_agent]).get_app()

# Function to initiate multimodal search and display the results
async def search_and_display(query: str):
    results = await multimodal_search(query)
    # Display or process the results
    print("Web Results:", results["web_results"])
    print("Video Results:", results["video_results"])

# Run the app and search for a sample query
if __name__ == "__main__":
    query = "example keyword to search"
    asyncio.run(search_and_display(query))
    serve_playground_app("search:app", reload=True)
