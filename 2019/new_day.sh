#! /bin/bash

DAY=$1
cat <<EOT >> ${DAY}a.py
from utils import readInput

#lines = readInput("input_${DAY}.txt")
lines = readInput("test.txt")

#print ("🎄Part 1: {}".format())
EOT

cat <<EOT >> ${DAY}b.py
from utils import readInput

#lines = readInput("input_${DAY}.txt")
lines = readInput("test.txt")

#print ("🎁🎄Part 2: {}".format())
EOT
