#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # Define the base URL of the API
    url = "https://jsonplaceholder.typicode.com/"
    # Get the employee ID from the command-line argument
    employee_id = sys.argv[1]
    # Send a GET request to the API to get the user data
    user = requests.get(url + "users/{}".format(employee_id)).json()
    # Send another GET request to the API to get the todos
    # data with the employee ID as a parameter
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Use a list comprehension to filter completed tasks and get their titles
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    # Print the first line of the output with the employee name,
    # number of completed tasks, and total number of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    # Use another list comprehension to print the titles of the completed
    # tasks with a tabulation and a space before each title
    [print("\t {}".format(c)) for c in completed]
