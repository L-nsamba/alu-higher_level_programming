#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status using urllib package.
It displays the body response with type, content, and utf8 content information.
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
