#!/bin/bash
# sends a DELETE request to the URL

response=$(curl -X DELETE -s "$1")

echo "$response"
