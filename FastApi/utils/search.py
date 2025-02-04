from serpapi import GoogleSearch


SERP_API_KEY="<SERP API>"

def search_content(topic):
    params = {
        "q": topic,
        "api_key": SERP_API_KEY,
        "num": 10 
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    content = ""
    for item in results["organic_results"]:
        content += f"{item['title']}\n{item['snippet']}\n{item['redirect_link']}\n"
    
    return content

def search_google_trends(country_code):
  params = {
    "engine": "google_trends_trending_now",
    "geo": country_code.replace("\n",''),
    "output": "JSON",
    "api_key": SERP_API_KEY
  }
  search = GoogleSearch(params)
  results = search.get_dict()
  results = results.get("trending_searches", [])
  trends = [result.get("query") for result in results[:3]]
  return trends