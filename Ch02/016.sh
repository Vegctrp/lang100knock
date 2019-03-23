#!/bin/sh -f

echo -n "input number"
read n

row=`wc -l ../data/hightemp.txt | cut -f 1 -d " "`

row_per_outfile=`expr $row / $n`
rem=`expr $row % $n`
if [ $rem -gt 0 ] ; then
    row_per_outfile=`expr $row_per_outfile + 1`
fi

split --lines=$row_per_outfile --numeric-suffixes=1 --additional-suffix=unix.txt ../data/hightemp.txt 016out