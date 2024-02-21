#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively prints a sorted count of given keywords
    in the titles of all hot articles for a given subreddit.
    """
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "custom_user_agent"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        # Count words in titles
        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    count_dict[word] = count_dict.get(
                            word, 0
                            ) + title.count(word)

        # Recursive call with the next page
        after = data.get("data", {}).get("after", None)
        if after:
            count_words(subreddit, word_list, after, count_dict)

    # Print the results after all pages have been processed
    if not after and count_dict:
        sorted_counts = sorted(
                count_dict.items(), key=lambda x: (-x[1], x[0])
                )
        for word, count in sorted_counts:
            print(f"{word}: {count}")
