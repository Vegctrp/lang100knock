#!/bin/sh
sort ./045result.txt | uniq -c | sort -n -r >045c1.txt
cat ./045result.txt | grep "する	"| sort | uniq -c | sort -n -r >045c2.txt
cat ./045result.txt | grep "見る	"| sort | uniq -c | sort -n -r >045c3.txt
cat ./045result.txt | grep "与える	"| sort | uniq -c | sort -n -r >045c4.txt