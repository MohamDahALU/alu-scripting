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
    response.header = "{\'Connection\': \'keep-alive\', \'Content-Length\': \'2955\', \'x-ua-compatible\': \'IE=edge\', \'content-type\': \'application/json; charset=UTF-8\', \'expires\': \'-1\', \'cache-control\': \'private, s-maxage=0, max-age=0, must-revalidate, no-store\', \'access-control-allow-origin\': \'*\', \'access-control-expose-headers\': \'X-Moose\', \'content-encoding\': \'gzip\', \'x-ratelimit-used\': \'2\', \'x-ratelimit-remaining\': \'98.0\', \'x-ratelimit-reset\': \'241\', \'Accept-Ranges\': \'bytes\', \'Date\': \'Fri, 21 Feb 2025 13:35:58 GMT\', \'Via\': \'1.1 varnish\', \'Vary\': \'accept-encoding\', \'Strict-Transport-Security\': \'max-age=31536000; includeSubdomains\', \'X-Content-Type-Options\': \'nosniff\', \'X-Frame-Options\': \'SAMEORIGIN\', \'X-XSS-Protection\': \'1; mode=block\', \'Set-Cookie\': \'loid=000000001jqjfa3t9f.2.1740144958431.Z0FBQUFBQm51SUUtTE1JOFRQVkRxd2Jha0d6ZjZHTWJ6UEV0WkNQX2gtZWJ5bTZWNmh5MmVJaTcyV2w1RGhQTUdheEwxZndlVEhHMUxqVTNXeWVKdFNfMjZ3eTZVR2lySHlNb0xTR2hSN0JkOEVrY2I4YlRsX2dWOUY2Q2JBcDRWQ0d6emphSDVOQ2M; Domain=reddit.com; Max-Age=63071999; Path=/; expires=Sun, 21-Feb-2027 13:35:58 GMT; secure; SameSite=None; Secure, session_tracker=bqfnhfcangaarpgbjg.0.1740144958444.Z0FBQUFBQm51SUUtaVhMU3UtUU5iWmVTb1NjUTdDM0VPQldtUHpSYVVVeEo1VnN6Rjh4TXZ3ZWpEQXhQSDY5ZmdqTXZFUENScjhycTFfMUhiSzQ5WVNEMVVRSXdQWGZ5aHlCS29LaGR4M1NWeFRvemJ5NHoxVklzNTJoN2RUMVBINHp5V0s2blRTRnA; Domain=reddit.com; Max-Age=7199; Path=/; expires=Fri, 21-Feb-2025 15:35:58 GMT; secure; SameSite=None; Secure, csv=2; Max-Age=63072000; Domain=.reddit.com; Path=/; Secure; SameSite=None, edgebucket=Kx7A21V6s4So7dckKi; Domain=reddit.com; Max-Age=63071999; Path=/;  secure\', \'Server\': \'snooserv\', \'Report-To\': \'{\"group\": \"w3-reporting-nel\", \"max_age\": 14400, \"include_subdomains\": true,  \"endpoints\": [{ \"url\": \"https://w3-reporting-nel.reddit.com/reports\" }]}, {\"group\": \"w3-reporting\", \"max_age\": 14400, \"include_subdomains\": true, \"endpoints\": [{ \"url\": \"https://w3-reporting.reddit.com/reports\" }]}, {\"group\": \"w3-reporting-csp\", \"max_age\": 14400, \"include_subdomains\": true, \"endpoints\": [{ \"url\": \"https://w3-reporting-csp.reddit.com/reports\" }]}\', \'NEL\': \'{\"report_to\": \"w3-reporting-nel\", \"max_age\": 14400, \"include_subdomains\": false, \"success_fraction\": 1.0, \"failure_fraction\": 1.0}\'}"

    
    if response.status_code != 200:
        print(None)
        return

    jsonData = response.json()
    data = jsonData["data"]["children"]
    for post in data:
        print(post.get("data", {}).get("title"))


top_ten("programming")
