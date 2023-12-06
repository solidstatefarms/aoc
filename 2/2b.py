#!/usr/bin/env python3
# Advent of Code day 2 part 2
# PFO

filename = "games.txt"
R = 12
G = 13
B = 14

total = 0
sumPower = 0

with open(filename) as f:
    for line in f:
        impossible = False
        green = 0
        red = 0
        blue = 0
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
                if data[1] == 'green' and int(data[0]) > green:
                    green = int(data[0])
                if data[1] == 'red' and int(data[0]) > red:
                    red = int(data[0])
                if data[1] == 'blue' and int(data[0]) > blue:
                    blue = int(data[0])
        sumPower += green * red * blue
        if not impossible:
            total += game
print(f'the total is: {total}')
print(f'the sum of the power is: {sumPower}')