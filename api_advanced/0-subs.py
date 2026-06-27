#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:alu.reddit.api:v1.0 (by /u/anonymous)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return 0

        return response.json()["data"]["subscribers"]

    except Exception:
        return 0