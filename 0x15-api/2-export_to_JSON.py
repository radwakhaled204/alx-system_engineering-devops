#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

# Import the json module to work with JSON files
import json
# Import the requests module to make HTTP requests
import requests
# Import the sys module to access command-line arguments
import sys

if __name__ == "__main__":
    # Get the user ID from the first command-line argument
    user_id = sys.argv[1]
    # Define the base URL of the web API
    url = "https://jsonplaceholder.typicode.com/"
    # Get the user data as a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()
    # Get the username from the user data
    username = user.get("username")
    # Get the to-do list data as a JSON object, filtering by user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Open a JSON file with the user ID as the name, in write mode
    with open("{}.json".format(user_id), "w") as jsonfile:
        # Dump the to-do list data as a JSON object to the file
        json.dump({user_id: [{
                # Each to-do item has the task, completion status,
                # and username fields
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
