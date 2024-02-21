#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively returns a list containing the titles of
    all hot articles for a given subreddit.
    If the subreddit is invalid or not found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "custom_user_agent"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        # Add titles to hot_list
        for post in posts:
            title = post.get("data", {}).get("title", "")
            hot_list.append(title)

        # Recursive call with the next page
        after = data.get("data", {}).get("after", None)
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
