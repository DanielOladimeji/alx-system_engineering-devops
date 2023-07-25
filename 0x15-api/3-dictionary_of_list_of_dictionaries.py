#!/usr/bin/python3
"""Export data in JSON format for all tasks from all employees"""
import json
import requests
import sys
import urllib


def get_all_employees_todos(url, userId):
    """export record to json file"""
    user_info = requests.get(url + "/users/{}".format(userId)).json()
    todos = requests.get(url + "/users/{}/todos/".format(userId)).json()
    username = user_info.get("username")
    tasks = []
    for task in todos:
        task_dic = {}
        task_dic["task"] = task.get("title")
        task_dic["completed"] = task.get("completed")
        task_dic["username"] = username
        tasks.append(task_dic)
    return tasks


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users/").json()
    dic = {}
    for user_info in users:
        dic[user_info.get("id")] = get_all_employees_todos(url, user_info.get("id"))
    with open("todo_all_employees.json", "w") as alljsonfile:
        json.dump(dic, alljsonfile)
