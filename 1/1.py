#!/usr/bin/env python3
# Advent of Code day 1
# PFO

filename = "calibration_values.txt"

total = 0

with open(filename) as f:
    for line in f:
        line = line.strip()
        print(line)
        line = list(line)
        num = []
        for character in line:
            try:
                value = int(character)
                num.append(value)
            except:
                pass
        print(num)
        print(f'{num[0]}', end='')
        digit1 = num[0]
        num.reverse()
        print(f'{num[0]}')
        digit2 = num[0]
        number = digit1 * 10 + digit2
        total += number
print(f'the total is {total}')


