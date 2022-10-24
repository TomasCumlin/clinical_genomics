#! /home/ete03/anaconda3/bin/python3

import sys

#import text file
f = open(sys.argv[1], "r")

print(f.name)

# boolean will turn true once the iteration passes "ORIGIN"
start = False

n_count = 0             # to store number of n

for line in f:
    if(start):                 # start counting n once iteration passes "ORIGIN"
        if bool(line):
            n_count += line.count("n")
    
    if "ORIGIN" in line:
        start = True

print(n_count)
