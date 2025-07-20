#!/bin/bash
# Sends GET request, displays body only for 200 status code
curl -s "$1" | grep -q "200" && curl -s "$1"
