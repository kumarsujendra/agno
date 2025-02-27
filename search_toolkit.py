from agno.tools import Toolkit
from youtube_search import YoutubeSearch
import json
import httpx

class SearchToolKit(Toolkit):

    def __init__(self, name="toolkit"):
        super().__init__(name="search_toolkit")
        # self.youtube_video_search(self.youtube_video_search)
        # self.get_top_stories(self.get_top_stories)
        self.product_search(self.product_search)       
        

    # def youtube_video_search(self, query: str, num_stories: int = 10) -> str:
    #     results = YoutubeSearch(query, max_results=num_stories).to_json()
    #     return json.dumps(results)
    
    
    def product_search(self, query: str, num_stories: int = 10) -> str:
        response = httpx.get(f'https://dummyjson.com/products/search?q={query}&limit={num_stories}', verify=False)
        results = response.json()
        return json.dumps(results)
    

    # def get_top_stories(self, num_stories: int = 10) -> str:
    #     # Fetch top story IDs
    #     response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    #     story_ids = response.json()

    #     # Fetch story details
    #     stories = []
    #     for story_id in story_ids[:num_stories]:
    #         story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    #         story = story_response.json()
    #         if "text" in story:
    #             story.pop("text", None)
    #         stories.append(story)
    #     return json.dumps(stories)
    
    

    
    
