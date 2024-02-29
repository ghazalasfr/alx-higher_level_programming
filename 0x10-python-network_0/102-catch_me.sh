#!/bin/bash
# This script message containing 'You got me!', in the body of the response.
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: BestSchool" -d "user_id=98"
