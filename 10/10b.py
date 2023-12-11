#!/usr/bin/env python3
# Advent of Code day 10 part 2
# PFO
import sys

routes = {'|':{'N': 'N', 'S':'S'},
          '-':{'E': 'E', 'W':'W'},
          'F':{'N': 'E', 'W':'S'},
          '7':{'N': 'W', 'E':'S'},
          'J':{'S': 'W', 'E':'N'},
          'L':{'S': 'E', 'W':'N'}}

def move(loc, d):
    if d == 'N':
        loc[0] -= 1
    elif d == 'E':
        loc[1] += 1
    elif d == 'S':
        loc[0] += 1
    elif d == 'W':
        loc[1] -= 1

def fillTilde():
    for row, line in enumerate(q):
        for col, char in enumerate(line):
            if row == 0 and char == ' ':
                q[row][col] = '~'
            elif char == ' ' and (up(row, col, q) == '~' or left(row, col, q) == '~'):
                q[row][col] = "~"

def up(r, c, q):
    if r == 0:
        return ''
    return q[r-1][c]
    
def left(r, c, q):
    if c == 0:
        return ''
    return q[r][c-1]
    
def right(r, c, q):
    if c == len(q[0]) - 1:
        return ''
    return q[r][c+1]
    
# process file into 2d array
filename = "pipes.txt"
p = []
q = []
with open(filename) as f:
    for line in f:
        p.append(list(line.strip()))
        q.append(list(' ' * len(line)))

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
q[location[0]][location[1]] = 'X'
direction = 'N' # found this by looking at the raw data
steps = 0
while True:
    move(location, direction)
    pipe = p[location[0]][location[1]]
    q[location[0]][location[1]] = 'X' # mark where we are
    steps += 1
    #print(f'pipe: {pipe} at row {location[0]} col {location[1]}')
    if pipe == 'S':
        break
    #print(f'direction: {direction}')
    direction = routes[pipe][direction]
    #print(f'new direction: {direction}')
    
print(f'total steps in the loop: {steps}')
print(f'half of that is: {steps / 2}')

# print a picture of the path
for line in q:
    for a in line:
        print(a, end='')
    print('')

fillTilde()
q.reverse()
fillTilde()
q = list(map(lambda x: x[::-1], q)) # https://stackoverflow.com/a/51839211/20736336
fillTilde()
q.reverse()
fillTilde()

innerCount = 0
for line in q:
    for a in line:
        print(a, end='')
        if a == ' ':
            innerCount += 1
    print('')


print(f'inner area: {innerCount}')
