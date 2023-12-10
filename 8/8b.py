#!/usr/bin/env python3
# Advent of Code day 8 part 2
# PFO
# discussion:
# lr = 'LRLRLR'
# len(lr) is 6
# if count is 6, then lr[6] is an error
# lr[6] should actually cause lr[0] to be looked up
# lr[7] should actually cause lr[1] to be looked up
# that can be calculated with count % len(lr)

def allEndInZ(n):
    #print(f'n is {n}')
    for i in n:
        #print(i)
        if not i[2] == 'Z':
            return False
        #print(i)
    return True
    
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

# get the list of nodes that end in A
node = []
for key in nodes:
    if key[2] == 'A':
        node.append(key)
print(node)

count = 0
llr = len(lr)
checkpoint = 1000000
while not allEndInZ(node):
    if count >= llr:
        lrcount = count % llr
    else:
        lrcount = count
    for i, n in enumerate(node):
        node[i] = nodes[n][lr[lrcount]]
    count += 1
    #print(node)
    if count == checkpoint:
        print(count)
        checkpoint += checkpoint
    
print(f'steps: {count}')