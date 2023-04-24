#!/usr/bin/python3
"""
This script uses a REST API to retrieve information about all users and their
corresponding tasks, and saves the data to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Define the REST API endpoint URLs.
    api_base_url = "https://jsonplaceholder.typicode.com/"
    users_url = api_base_url + "users"
    todos_url = api_base_url + "todos"

    # Make the API requests to get the users and tasks data.
    users_data = requests.get(users_url).json()
    todos_data = requests.get(todos_url).json()

    # Create a dictionary to store the tasks for each user.
    tasks_by_user = {}
    for user in users_data:
        tasks = []
        for task in todos_data:
            if task["userId"] == user["id"]:
                task_dict = {"username": user["username"],
                             "task": task["title"],
                             "completed": task["completed"]}
                tasks.append(task_dict)
        tasks_by_user[user["id"]] = tasks

    # Write the tasks_by_user dictionary to a JSON file.
    with open("todo_all_employees.json", "w") as f:
        json.dump(tasks_by_user, f)
