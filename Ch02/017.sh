#!/bin/sh -f

cut -f 1 ../data/hightemp.txt | sort | uniq >017outunix.txt

python3 017.py | sort > 017out.txt

diff --report-identical-files 017outunix.txt 017out.txt