#!/usr/bin/python3
"""Takes in a URL and an email address, sends a
POST request to the passed URL with the email
"""

from sys import argv
import requests


if __name__ == "__main__":
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)

    print(req.text)
