#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or not found, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "custom_user_agent"}

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        # Print titles of the first 10 posts
        for post in posts:
            title = post.get("data", {}).get("title", "")
            print(title)
    else:
        print(None)
