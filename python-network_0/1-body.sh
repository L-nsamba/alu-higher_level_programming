#!/bin/bash
# Sends GET request, displays body only for 200 status code
curl -sL -w "%{http_code}" "$1" -o /tmp/body | grep -q 200 && cat /tmp/body
