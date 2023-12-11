#!/usr/bin/env python3
# Advent of Code day 3
# PFO

def around(row, start, end):
    if start == 0:
        start += 1
    if end == len(schem[0]) - 1:
        end -= 1
    if row == 0:
        rows = [row, row + 1]
    elif row == len(schem) - 1:
        rows = [row - 1, row]
    else:
        rows = [row - 1, row, row + 1]
    for R in rows:
        for i in range(start - 1, end + 2):
            if schem[R][i] in symbols:
                return True
    return False
    
filename = "schematic.txt"
schem = []
s = []
with open(filename) as f:
    for line in f:
        schem.append(line.strip())
        s.append(list(line.strip()))

symbols = []
for row in s:
    for character in row:
        if not character.isdecimal() and not character == '.' and not character in ''.join(symbols):
            symbols.append(character)
print(symbols)

total = 0
skip = 0
for row, line in enumerate(schem):
    for i in range(len(schem[0])):
        if skip:
            skip -= 1
            continue
        if line[i].isdecimal():
            numberString = ''
            start = i
            pos = i
            while line[pos].isdecimal():
                numberString += line[pos]
                pos += 1
                skip += 1
                if pos >= len(schem[0]):
                    break
            end = pos - 1
            print(f"found Number {numberString}")
            print(start)
            print(end)
            symb = around(row, start, end)
            print(symb)
            if symb:
                total += int(numberString)
                
print(f'total is: {total}')