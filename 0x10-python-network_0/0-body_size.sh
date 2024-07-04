#!/bin/bash
# Get the byte size of the HTTP responses for the header for a given URL.
curl -s "$1" | wc -c
