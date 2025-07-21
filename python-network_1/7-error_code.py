#!/usr/bin/python3
"""
This module sends a request to a URL using the requests package and displays
the body of the response. If the HTTP status code is >= 400, it displays
the error code instead.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
