#!/bin/bash

# Send a POST request to the specified URL and write the response to a temporary file
curl -sX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -o response.txt >/dev/null 2>&1 &

# Wait for the background process to complete
wait %1

# Check if the temporary file contains the message and display it
grep -q "You got me!" response.txt && rm response.txt
