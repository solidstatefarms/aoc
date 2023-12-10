#!/usr/bin/env python3
# Advent of Code day 9 part 2
# PFO

def makeSeq(seq):
    nextSeq = []
    #if len(seq) > 1:
    for i in range(len(seq) - 1):
        nextSeq.append(seq[i+1] - seq[i])
    return nextSeq

def isAllZero(seq):
    for i in seq:
        if not i == 0:
            return False
    return True
    
filename = "report.txt"
with open(filename) as f:
    report = f.readlines()
    print(report)
readings = []
for line in report:
    lineArray = []
    for value in line.strip().split():
        lineArray.append(int(value))
    readings.append(lineArray)
print(readings)

total = 0
for line in readings:
    progression = []
    progression.append(line)
    while not isAllZero(line):
        print(line)
        line = makeSeq(line)
        progression.append(line)
    #print(progression)
    # now work our way back up
    progression.reverse()
    addend = 0
    for line in progression:
        print(line)
        addend = line[0] - addend
    total += addend    
    
print(f'total of previous values is: {total}')