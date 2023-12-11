#!/usr/bin/env python3
# Advent of Code day 10
# PFO

routes = {'|':{'N': 'N', 'S':'S'},
          '-':{'E': 'E', 'W':'W'},
          'F':{'N': 'E', 'W':'S'},
          '7':{'N': 'W', 'E':'S'},
          'J':{'S': 'W', 'E':'N'},
          'L':{'S': 'E', 'W':'N'}}
print(routes)

def move(loc, d):
    if d == 'N':
        loc[0] -= 1
    elif d == 'E':
        loc[1] += 1
    elif d == 'S':
        loc[0] += 1
    elif d == 'W':
        loc[1] -= 1

# process file into 2d array
filename = "pipes.txt"
p = []
with open(filename) as f:
    for line in f:
        p.append(list(line.strip()))

# find where we are starting
for row, line in enumerate(p):
    if 'S' in line:
        #print(line)
        print(f'S is in row: {row}')
        r = row
        for col, character in enumerate(line):
            if character == 'S':
                print(f'S is at col: {col}')
                c = col

location = [r, c]
direction = 'N' # found this by looking at the raw data
steps = 0
while True:
    move(location, direction)
    pipe = p[location[0]][location[1]]
    steps += 1
    print(f'pipe: {pipe} at row {location[0]} col {location[1]}')
    if pipe == 'S':
        break
    print(f'direction: {direction}')
    direction = routes[pipe][direction]
    print(f'new direction: {direction}')
    
print(f'total steps in the loop: {steps}')
print(f'half of that is: {steps / 2}')