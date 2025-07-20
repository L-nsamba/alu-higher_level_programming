#!/bin/bash
# Sends GET request with custom header and displays response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
