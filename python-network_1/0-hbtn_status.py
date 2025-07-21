#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status and displays the body
response with type information and content in both bytes and UTF-8 format.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
