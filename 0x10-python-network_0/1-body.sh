#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -sL "$1" -o /dev/null -w "%{http_code}" | grep -q "200" && curl -sL "$1"
