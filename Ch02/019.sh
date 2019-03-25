#!/bin/sh -f

cut -f 1 ../data/hightemp.txt | sort | uniq -c | sort -r