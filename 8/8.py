#!/usr/bin/env python3
# Advent of Code day 8
# PFO
# discussion:
# lr = 'LRLRLR'
# len(lr) is 6
# if count is 6, then lr[6] is an error
# lr[6] should actually cause lr[0] to be looked up
# lr[7] should actually cause lr[1] to be looked up
# that can be calculated with count % len(lr)
filename = "map.txt"
with open(filename) as f:
    m = f.readlines()
lr = list(m[0].strip())
del m[0]
del m[0]
nodes = {}
for line in m:
    nodes[line[:3]] = {'L':line[7:10], 'R':line[12:15]}
    
print(lr)
print(nodes)

node = 'AAA'
count = 0
while not node == 'ZZZ':
    if count >= len(lr):
        lrcount = count % len(lr)
    else:
        lrcount = count
    nextNode = nodes[node][lr[lrcount]]
    node = nextNode
    count += 1
    
print(f'steps: {count}')