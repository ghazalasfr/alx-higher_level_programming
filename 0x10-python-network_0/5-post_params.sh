#!/bin/bash
# of the response. A variable 'email' be sent with the value 'I will always be here for PLD'.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
