#!/usr/bin/python3
"""
   returns a list containing titles of hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """a recursive function to return the titles of hot arcticles
       for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    custom_headers = {
               "User-Agent":
               "ubuntu4.20:0x16-api:v1.0.0 (by /u/oluwasube)"
              }
    try:
        response = requests.get(url,
                                headers=custom_headers,
                                allow_redirects=False).json()
        post_list = response["data"]["children"]
        for post in post_list:
            hot_list.append(post["data"]["title"])
        if response["data"]["after"] is None:
            return hot_list
        return recurse(subreddit, hot_list, response["data"]["after"])
    except Exception:
        return None
