#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status using the requests
module and displays the body response with type and content information.
"""

import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
