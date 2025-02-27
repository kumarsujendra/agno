# from agno.agent import Agent
# from agno.model.openai import OpenAIChat
# from agno.storage.agent.sqlite import SqlAgentStorage
# from agno.tools.duckduckgo import DuckDuckGo
# from agno.tools.yfinance import YFinanceTools
# from agno.playground import Playground, serve_playground_app

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

import json
import httpx
from youtube_search import YoutubeSearch

def search_youtube_videos(query: str) -> str:
    # results = YoutubeSearch(query, max_results=num_stories).to_json()
    # return json.dumps(results)
    response = httpx.get(f'https://dummyjson.com/products/search?q={query}')
    results = response.json()
    return json.dumps(results)    



def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

agent = Agent(
    name="Search Agent",
    agent_id="search_agent",
    role="Search News and Videos",
    # tools=[get_top_hackernews_stories, search_youtube_videos], 
    tools=[get_top_hackernews_stories], 
    show_tool_calls=True, 
    markdown=True)

# agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("top_stories:app", reload=True)
 