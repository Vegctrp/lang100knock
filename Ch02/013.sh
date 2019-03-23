#!/bin/sh -f

paste ./col1.txt ./col2.txt > 013result_test.txt

diff -s ./013result.txt ./013result_test.txt