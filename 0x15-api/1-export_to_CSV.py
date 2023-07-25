#!/usr/bin/python3
"""Using script from 0-gather_data_from_an_API.py, exxport data in the CSV format"""
import requests
import sys
import urllib
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_info = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/users/{}/todos/".format(sys.argv[1])).json()
    username = user_info.get("username")
    with open("{}.csv".format(sys.argv[1]), "w", encoding="UTF8",
              newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            task_status = task.get("completed")
            task_title = task.get("title")
            writer.writerow([sys.argv[1], username, task_status, task_title])
