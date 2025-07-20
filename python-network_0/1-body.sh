#!/bin/bash
# Sends a GET request to a URL and displays response body only for 200 status codes
[ "$(curl -s -L -w "%{http_code}" -o /tmp/response "$1")" = "200" ] && cat /tmp/response
