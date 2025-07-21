#!/usr/bin/python3
"""
This module sends a POST request to search for users with a letter parameter
and displays the results in JSON format, handling various response scenarios.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            user_id = json_response.get('id')
            user_name = json_response.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
