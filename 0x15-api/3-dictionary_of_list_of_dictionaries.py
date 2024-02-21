#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

# Import the json module to work with JSON files
import json
# Import the requests module to make HTTP requests
import requests

if __name__ == "__main__":
    # Define the base URL of the web API
    url = "https://jsonplaceholder.typicode.com/"
    # Get the user data as a JSON object
    users = requests.get(url + "users").json()

    # Open a JSON file with the name "todo_all_employees.json", in write mode
    with open("todo_all_employees.json", "w") as jsonfile:
        # Dump the to-do list data of all employees
        # as a JSON object to the file
        json.dump({
            # For each user, get their ID, username, and to-do list data
            u.get("id"): [{
                # Each to-do item has the task, completion status,
                # and username fields
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    # Filter the to-do list data by user ID
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
