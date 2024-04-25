#!/bin/bash

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq '.' "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON: $2"
    exit 1
fi

# Send the JSON POST request and display the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
