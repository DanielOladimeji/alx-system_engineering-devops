#!/usr/bin/python3
"""Using task 0-gather_data_from_an_API.py, export data in the JSON format"""
import requests
import sys
import urllib
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_info = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/users/{}/todos/".format(sys.argv[1])).json()
    username = user_info.get("username")
    dic = {}
    tasks = []
    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        for task in todos:
            task_dic = {}
            task_dic["task"] = task.get("title")
            task_dic["completed"] = task.get("completed")
            task_dic["username"] = username
            tasks.append(task_dic)
        dic[sys.argv[1]] = tasks
        json.dump(dic, jsonfile)
