#!/bin/sh -f

echo -n "input num"
read n
tail -n $n ../data/hightemp.txt