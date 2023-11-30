#!/bin/bash
#  sends a GET request to the URL, and displays the body
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl "$1"
