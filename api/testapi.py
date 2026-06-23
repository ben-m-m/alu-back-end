#!/usr/bin/python3
"""Returns number of subscribers for a subreddit."""
import requests

HEADERS = {
    "User-Agent": "linux:reddit_api_practice:v1.0 (by /u/Web_Dev_24)"
}

def number_of_subscribers(subreddit):
    """Return subscriber count or 0 if invalid subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=HEADERS, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

#!/usr/bin/python3
"""Prints titles of top 10 hot posts."""
import requests

HEADERS = {
    "User-Agent": "linux:reddit_api_practice:v1.0 (by /u/Web_Dev_24)"
}

def top_ten(subreddit):
    """Print top 10 hot post titles or None."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)

#!/usr/bin/python3
"""Recursively fetch all hot post titles."""
import requests

HEADERS = {
    "User-Agent": "linux:reddit_api_practice:v1.0 (by /u/Web_Dev_24)"
}

def recurse(subreddit, hot_list=None, after=None):
    """Return list of all hot post titles or None if invalid."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        title = post.get("data", {}).get("title")
        if title:
            hot_list.append(title)

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)


#!/usr/bin/python3
"""Count keyword occurrences in hot Reddit posts."""
import requests
import re
from collections import defaultdict

HEADERS = {
    "User-Agent": "linux:reddit_api_practice:v1.0 (by /u/your_username)"
}

def recurse_titles(subreddit, after=None, titles=None):
    """Helper: recursively collect titles."""
    if titles is None:
        titles = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        titles.append(title)

    if data.get("after") is None:
        return titles

    return recurse_titles(subreddit, data.get("after"), titles)


def count_words(subreddit, word_list):
    """Print word counts sorted by frequency and alphabet."""
    titles = recurse_titles(subreddit)

    if titles is None:
        return

    counts = defaultdict(int)

    word_list = [w.lower() for w in word_list]

    for title in titles:
        words = re.findall(r"\w+", title.lower())
        for w in words:
            if w in word_list:
                counts[w] += 1

    if not counts:
        return

    sorted_counts = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        print(f"{word}: {count}")