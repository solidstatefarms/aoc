#!/usr/bin/env python3
# Advent of Code day 2
# PFO

filename = "games.txt"
R = 12
G = 13
B = 14

total = 0

with open(filename) as f:
    for line in f:
        impossible = False
        game = int(line.split(':')[0].split(' ')[-1])
        print(f'Game: {game}')
        sets  = line.strip().split(':')[1].split(';')
        #print(sets)
        for sett in sets:
            #print(sett)
            colors = sett.strip().split(',')
            for color in colors:
                data = color.strip().split(' ')
                print(data)
                if data[1] == 'green' and int(data[0]) > G or data[1] == 'red' and int(data[0]) > R or data[1] == 'blue' and int(data[0]) > B:
                    impossible = True
                    print('found impossible game')
        if not impossible:
            total += game
print(f'the total is: {total}')