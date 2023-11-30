#!/bin/bash
# sends a POST request to the passed URL, and displays the body
val1="test@gmail.com"
val2="I will always be here for PLD"

curl -X POST -d "email=$val1&subject=$val2" "$1"
