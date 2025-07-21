#!/usr/bin/python3
"""Fetches a URL and displays the response body content, type, and UTF-8 decoding."""

import urllib.request


def fetch_status():
    """Fetches and prints the body of the response from a given URL."""
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
