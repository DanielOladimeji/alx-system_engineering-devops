#!/usr/bin/python3
""" prints a sorted count of given keywords  """
import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """ Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None
    """
    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for x in range(len(word_list)):
                    if word_list[x].lower() == word.lower():
                        count[x] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for x in range(len(word_list)):
                for y in range(x + 1, len(word_list)):
                    if word_list[x].lower() == word_list[y].lower():
                        save.append(j)
                        count[x] += count[y]

            for x in range(len(word_list)):
                for y in range(x, len(word_list)):
                    if (count[y] > count[x] or
                            (word_list[x] > word_list[y] and
                             count[y] == count[x])):
                        aux = count[x]
                        count[x] = count[y]
                        count[y] = aux
                        aux = word_list[x]
                        word_list[x] = word_list[y]
                        word_list[y] = aux

            for x in range(len(word_list)):
                if (count[x] > 0) and x not in save:
                    print("{}: {}".format(word_list[x].lower(), count[x]))
        else:
            count_words(subreddit, word_list, after, count)
