#!/usr/bin/python3
"""queries REDDIT API and returns the total number of subsrcibers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subcribers on a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    custom_headers = {
               "User-Agent":
               "ubuntu4.20:0x16-api:v1.0.0 (by /u/oluwasube)"
              }
    try:
        response = requests.get(url,
                                headers=custom_headers,
                                allow_redirects=False).json()
        return response["data"]["subscribers"]
    except Exception:
        return 0
