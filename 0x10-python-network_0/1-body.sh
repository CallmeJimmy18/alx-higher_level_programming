#!/usr/bin/bash
#  sends a GET request to the URL, and displays the body

response=$(curl -L -s "$1")

status_code=$(echo "$response" | grep -Fi HTTP/ | awk '{print $2}')
if [ "$status_code" -eq 200 ]; then
	echo "$response" | awk '/^$/{flag=1; next} flag{print}'
fi
