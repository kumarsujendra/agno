# from youtube_search import YoutubeSearch
# results = YoutubeSearch('search terms', max_results=10).to_json()
# print(results)


from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("agno")
print(response)
# for result in response.results:
#     print("Title: " + result.title)
#     print("Content: " + result.getText())
