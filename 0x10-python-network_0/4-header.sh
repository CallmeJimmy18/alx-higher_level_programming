#!/bin/bash
# sends a GET request to the URL, and displays the body
x_school_user_id=98; curl -X GET -H "X-School-User-Id: $x_school_user_id" "$1"
