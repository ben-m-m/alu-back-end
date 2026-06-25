#!/usr/bin/python3
"""Get employee data.
First line:
Employee EMPLOYEE_NAME is done with tasks(DONE_TASKS/TOTAL_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS:
total number of tasks, which is the sum of completed and non-completed tasks
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(user_url).json()

    # Get employee todos
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos = requests.get(todos_url).json()

    # Build the list of tasks
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    # Create the required JSON structure
    data = {
        employee_id: tasks
    }

    # Write to USER_ID.json
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(data, json_file)
