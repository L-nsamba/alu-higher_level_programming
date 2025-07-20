#!/bin/bash
# Displays all HTTP methods accepted by the server for given URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
