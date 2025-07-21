#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status using urllib package.
It displays the body response with type, content, and utf8 content information.
"""
import urllib.request


if __name__ == "__main__":
    """
    Fetches the status from https://alu-intranet.hbtn.io/status
    and displays the response body information.
    """
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
