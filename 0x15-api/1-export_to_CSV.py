#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

# Import the csv module to work with CSV files
import csv
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

    # Open a CSV file with the user ID as the name, in write mode
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create a CSV writer object with quoting enabled
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write a row to the CSV file for each to-do item
        for t in todos:
            # The row consists of the user ID, username, completion status,
            # and title of the to-do item
            writer.writerow(
                    [user_id, username, t.get("completed"), t.get("title")]
                    )
