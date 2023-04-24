#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    user_response = requests.get(url_users, params={'id': employee_id})
    todos_response = requests.get(url_todos, params={'userId': employee_id})

    try:
        employee_name = user_response.json()[0].get('username')
    except:
        print("Employee doesn't exist")
        exit()

    tasks_list = []
    for task in todos_response.json():
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = employee_name
        tasks_list.append(task_dict)

    employee_dict = {employee_id: tasks_list}

    filename = employee_id + ".json"
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(employee_dict, file)
