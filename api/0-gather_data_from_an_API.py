#!/usr/bin/python3

import requests
import sys
"""Get employee data"""

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(user_url).json()

    # Get employee todos
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos = requests.get(todos_url).json()

    # Filter completed tasks
    completed = [task for task in todos if task.get("completed")]

    # Print summary
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(completed),
            len(todos)
        )
    )

    # Print completed task titles
    for task in completed:
        print("\t {}".format(task.get("title")))