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
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    try:
        json = response.json()
        data = json["data"]["children"]
        if not data:
            print(None)
            return
        for post in data:
            print(post.get("data", {}).get("title"))
    except (KeyError, ValueError):
        print(None)


# top_ten("sudan")
