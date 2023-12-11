#!/usr/bin/env python3
# Advent of Code day 3 part 2
# PFO

gears = []

def checkGear(row, start, end, number):
    # adjust start and end if they are at edge
    if start == 0:
        start += 1
    if end == len(schem[0]) - 1:
        end -= 1
    # adjust rows to search if at top or bottom
    if row == 0:
        rows = [row, row + 1]
    elif row == len(schem) - 1:
        rows = [row - 1, row]
    else:
        rows = [row - 1, row, row + 1]
    for R in rows:
        print(f'checking row {R}')
        for col in range(start - 1, end + 2):
            isAGear(R, col, number)
    
def isAGear(row, col, number):
    for i, gear in enumerate(gears):
        if gear['R'] == row and gear['C'] == col:
            gears[i]['nums'].append(number) 

filename = "schematic.txt"
schem = []
with open(filename) as f:
    for line in f:
        schem.append(line.strip())

# first find where the gears are
for row, line in enumerate(schem):
    for i in range(len(schem[0])):
        if '*' == line[i]:
            gears.append({'R':row, 'C':i, 'nums': []})

skip = 0
for row, line in enumerate(schem):
    print(f'ROW: {row}')
    for i in range(len(schem[0])):
        if skip:
            skip -= 1
            continue
        if line[i].isdecimal():
            numberString = ''
            start = i
            pos = i
            print(i)
            while line[pos].isdecimal():
                numberString += line[pos]
                pos += 1
                skip += 1
                if pos >= len(schem[0]):
                    break
            end = pos - 1
            print(f"found Number {numberString} at {start}-{end}")
            checkGear(row, start, end, int(numberString))

print(gears)

total = 0
for gear in gears:
    if len(gear['nums']) == 2:
        total += gear['nums'][0] * gear['nums'][1]
        
print(f'total of gear ratios is: {total}')