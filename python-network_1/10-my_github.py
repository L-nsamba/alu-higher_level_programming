#!/usr/bin/python3
"""
This module uses the GitHub API with Basic Authentication to display the
user ID of the authenticated user using username and personal access token.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print("None")
