#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status using urllib package.
It displays the body response with type, content, and utf8 content information.
"""
import urllib.request


if __name__ == "__main__":
    """
    Fetches the status from the available URL
    and displays the response body information.
    """
    urls = [
        "https://alu-intranet.hbtn.io/status",
        "https://intranet.hbtn.io/status",
        "http://0.0.0.0:5050/status"
    ]

    body = None
    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read()
                break
        except (urllib.error.URLError, ConnectionRefusedError, OSError):
            continue

    if body is not None:
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
