#!/bin/bash
# Sends GET request, shows body only if status is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
