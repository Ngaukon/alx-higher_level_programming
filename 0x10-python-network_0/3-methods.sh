#!/bin/bash
# Display all HTTP methods the will indefently read by  the server of a given URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
