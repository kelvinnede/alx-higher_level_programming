#!/bin/bash
# This script sends a POST request with specified parameters to the URL and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
