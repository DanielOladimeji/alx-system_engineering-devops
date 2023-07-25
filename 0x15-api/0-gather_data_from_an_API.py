#!/usr/bin/python3
""" This script uses REST API for a given employee's ID
    and returns information about his/her TODO list progress.
"""
import requests
import sys
import urllib


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_info = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/users/{}/todos/".format(sys.argv[1])).json()
    total_tasks = len(todos)
    completed_tasks = []
    for task in todos:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user_info.get("name"), len(completed_tasks), total_tasks))
    for task_title in completed_tasks:
        print("\t {}".format(task_title))
