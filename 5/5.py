#!/usr/bin/env python3
# Advent of Code day 5
# PFO

filename = "almanac.txt"

lowestLocation = {'seed': 0, 'location': 0}

with open(filename) as f:
    for line in f:
        if line[:5] == 'seeds':
            seeds = line.strip().split(':')[1].strip().split(' ')
            for i in range(len(seeds)):
                seeds[i] = int(seeds[i])
            print(f"Seeds: {seeds}")
s = {}
for seed in seeds:
    s[seed] = {'seed': seed, 'soil': 0, 'fertilizer': 0, 'water': 0, 'light': 0, 'temperature': 0, 'humidity': 0, 'location': 0}
    for nxt in s[seed]:
        if nxt == 'seed':
            prv = nxt
            continue
        with open(filename) as f:
            mapFound = False
            # process the next map
            theMap = []
            for line in f:
                if mapFound and line.strip() == '':
                    break
                if mapFound:
                    theMap.append(line.strip().split(' '))
                if prv in line and nxt in line:
                    mapFound = True
                    print(f'found map {prv}-to-{nxt}')
            #print(theMap)
            # do default
            s[seed][nxt] = s[seed][prv]
            # see where our prv falls in this map
            for mapLine in theMap:
                if s[seed][prv] >= int(mapLine[1]) and s[seed][prv] < int(mapLine[1]) + int(mapLine[2]):
                    print('found it in theMap')
                    s[seed][nxt] = int(mapLine[0]) + s[seed][prv] - int(mapLine[1])
        if nxt == 'location' and s[seed][nxt] < lowestLocation['location'] or lowestLocation['seed'] == 0:
            lowestLocation['seed'] = seed
            lowestLocation['location'] = s[seed][nxt]
        prv = nxt
print(s)
print(lowestLocation)
