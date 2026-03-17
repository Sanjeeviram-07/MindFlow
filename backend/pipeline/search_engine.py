import requests

def search_topic(topic):

    url = f"https://api.duckduckgo.com/?q={topic}&format=json"

    response = requests.get(url).json()

    if response.get("AbstractURL"):
        return response["AbstractURL"]

    return None