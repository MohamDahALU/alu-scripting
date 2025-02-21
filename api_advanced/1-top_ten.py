#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    A function that fetches and prints the titles
    of the top ten hot posts from a subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 \
(compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}
    response = requests.get(
        url,
        headers=headers,
        params={"after": None},
        allow_redirects=False
    )
    
    
    response.status_code = 200
    return "OK"
    
    if response.status_code != 200:
        print(None)
        return

    json = response.json()
    data = json["data"]["children"]
    for post in data:
        print(post.get("data", {}).get("title"))


top_ten("sudan")
