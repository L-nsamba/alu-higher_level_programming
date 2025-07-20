#!/bin/bash
# This script sends a request to a URL and displays the response body size in bytes
curl -s "$1" | wc -c
