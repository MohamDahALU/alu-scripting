#!/usr/bin/python3
"""
This module contains a function to get the number
of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of
    subscribers for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data["data"]["subscribers"]
    else:
        return 0
