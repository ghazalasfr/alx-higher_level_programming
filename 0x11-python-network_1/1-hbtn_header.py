#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
that variable found in the header of the response.
"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request(argv[1])

    with urlopen(req) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
