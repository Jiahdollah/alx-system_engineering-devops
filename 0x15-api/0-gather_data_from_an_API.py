#!/usr/bin/python3
"""
Using this REST API (https://jsonplaceholder.typicode.com/), for a given employee ID,
returns information about his/her TODO list progress.
"""

import sys
import requests

if __name__ == '__main__':
    # Check if user provided the employee ID as a parameter
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        exit(1)

    # Get the employee ID from the command line
    employee_id = sys.argv[1]

    # Make API requests to retrieve the employee name and TODO list
    employee_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    todos_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))

    # Parse the JSON responses
    employee = employee_request.json()
    todos = todos_request.json()

    # Count the number of completed tasks
    completed_tasks = [task for task in todos if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Print the employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee['name'], num_completed_tasks, len(todos)))

    # Print the titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task['title']))

