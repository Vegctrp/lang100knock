#!/bin/sh -f

sed 's/\t/ /g' ../data/hightemp.txt

tr '\t' ' ' <../data/hightemp.txt

expand -t 1 ../data/hightemp.txt