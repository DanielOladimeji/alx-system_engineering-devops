#!/usr/bin/python3
"""queries REDDIT API and returns top 10 posts of a given subreddit"""
import requests


def top_ten(subreddit):
    """list of titles for the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    custom_headers = {
               "User-Agent":
               "ubuntu4.20:0x16-api:v1.0.0 (by /u/oluwasube)"
              }
    try:
        response = requests.get(url,
                                headers=custom_headers,
                                allow_redirects=False).json()
        posts = response["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print("None")
