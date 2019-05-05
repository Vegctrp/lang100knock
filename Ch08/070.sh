#!/bin/sh
cat ./sentiment.txt | cut -f 1 -d ' ' | sort | uniq -c