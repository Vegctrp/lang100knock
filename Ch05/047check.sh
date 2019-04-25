#!/bin/sh
cat ./047result.txt | cut -f 1 | sort | uniq -c | sort -n -r > 047c1.txt

cat ./047result.txt | cut -f 1,2 | sort | uniq -c | sort -n -r > ./047c2.txt