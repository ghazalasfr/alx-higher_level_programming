#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
with `requests` module
"""

import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as site:
        html = site.read()

    print('Body response:')
    print("\t- type:", type(html))
    print("\t- content:", html)

