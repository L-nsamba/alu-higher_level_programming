#!/usr/bin/python3
"""
This module sends a request to a URL
and displays the X-Request-Id header value.
It takes a URL as a command line argument
and uses urllib to make the request.
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
