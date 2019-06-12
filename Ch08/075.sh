#!/bin/sh

echo "worst 10:"
cat ./073result.txt | sort -nk 2,2 | head --lines=10
echo "top 10:"
cat ./073result.txt | sort -nrk 2,2 | head --lines=10