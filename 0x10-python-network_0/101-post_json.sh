#!/bin/bash
# Sends a JSON POST request to the given URL with a given JSON files.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
