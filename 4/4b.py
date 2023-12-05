#!/usr/bin/env python3
# Advent of Code day 4 part 2
# PFO
import re

filename = "cards.txt"
score = 0

copies = [0]
with open(filename) as f:
    for line in f:
        copies.append(1)
        
with open(filename) as f:
    for line in f:
        card = int(line.split(':')[0].split(' ')[-1])
        winning = line.split(':')[1].split('|')[0].strip()
        have = line.split('|')[1].strip()
        print(f'Card: {card}')
        # get rid of double spaces
        winning = re.sub(r'  ', r' ', winning)
        have = re.sub(r'  ', r' ', have)
        print(winning)
        print(have)
        winning = winning.split(' ')
        have = have.split(' ')
        match = 0
        for num in winning:
            if num in have:
                match += 1
        if match:
            score += 2**(match-1)
            print(2**(match-1))
            # increment copies of cards
            for j in range(copies[card]):
                for i in range(match):
                    copies[card+i+1] += 1
        else:
            print(0)
        
print(f'total score is: {score}')

cards = 0
for i in copies:
    cards += i
    
print(f'total cards: {cards}')
