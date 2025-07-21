#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status and displays:
- type of the response
- raw byte content
- decoded utf-8 content
"""

import urllib.request


def fetch_status():
    """Sends a request to the specified URL and
       prints the formatted response."""
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
