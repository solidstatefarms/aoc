#!/usr/bin/env python3
# Advent of Code day 7 part 2
# PFO
import re
import copy
import sys
filename = "hands.txt"
hands = []
with open(filename) as f:
    for line in f:
        hands.append([a for a in line.strip().split()])
#highCard = copy.deepcopy(hands)

# find five of a kind
fiveKind = []
remaining5 = []
for hand, bid in hands:
    foundFive = False
    # find how many J
    rx = re.compile('J')
    Jcount = len(rx.findall(hand))
    # look through the hand
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if hand == 'JJJJJ' or count + Jcount == 5:
            #print('found five of a kind')
            foundFive = True
    if foundFive:
        fiveKind.append([hand, int(bid)])
    else:
        remaining5.append([hand, int(bid)])
print('five of a kind')
print(fiveKind)
print('remaining5')
print(remaining5)

# find four of a kind
fourKind = []
remaining4 = []
for hand, bid in remaining5:
    foundFour = False
    # find how many J
    rx = re.compile('J')
    Jcount = len(rx.findall(hand))
    # look through the hand
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if not card == 'J' and count + Jcount == 4:
            #print('found four of a kind')
            foundFour = True
    if foundFour:        
        fourKind.append([hand, int(bid)])
    else:
        remaining4.append([hand, int(bid)])
print('four of a kind')
print(fourKind)
print('remaining4')
print(remaining4)

# find full house and three of a kind
# J can't be more than two now
fullHouse = []
threeKind = []
remaining3 = []
for hand, bid in remaining4:
    # find how many J
    rx = re.compile('J')
    Jcount = len(rx.findall(hand))
    # look through the hand
    foundThree = False
    foundTwo = 0
    print(hand)
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if count == 3:
            #print('found three of a kind')
            foundThree = True
        if count == 2 and not card == 'J':
            #print('found two of a kind not J')
            foundTwo += 1
    if Jcount == 1 and foundTwo == 4 or Jcount == 2 and foundTwo == 2 or foundThree and foundTwo:
        print("fullhouse")
        fullHouse.append([hand, int(bid)])
    elif Jcount == 1 and foundTwo or Jcount == 2 or foundThree:
        print("threekind")
        threeKind.append([hand, int(bid)])
    else:
        remaining3.append([hand, int(bid)])
print('full house')
print(fullHouse)
print('three of a kind')
print(threeKind)
print('remaining3')
print(remaining3)

# find two pair and one pair
# J can only be zero or one now
twoPair = []
onePair = []
remaining2 = []
for hand, bid in remaining3:
    # find how many J
    rx = re.compile('J')
    Jcount = len(rx.findall(hand))
    # look through the hand
    foundTwo = 0
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if count == 2:
            print('found two of a kind')
            foundTwo += 1
    if Jcount == 1 and foundTwo == 2 or foundTwo == 4:
        twoPair.append([hand, int(bid)])
    elif Jcount == 1 or foundTwo == 2:
        onePair.append([hand, int(bid)])
    else:
        remaining2.append([hand, int(bid)])
print('twopair')
print(twoPair)
print('onepair')
print(onePair)
print('remaining2')
print(remaining2)

# compute a strength value for each hand
# expand each char to two digits, and also the type
# and then append to create a base 10 integer
# X1,234,567,890
# append this to each hand and bid array as a third element
nums = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A':14}
master = []
for j, t in enumerate([remaining2, onePair, twoPair, threeKind, fullHouse, fourKind, fiveKind]):
    for i, handBid in enumerate(t):
        strength = 0
        multiplier = 1
        backwardsHand = list(handBid[0])
        backwardsHand.reverse()
        for c in backwardsHand:
            try:
                value = int(c)
            except:
                value = nums[c]
            strength += multiplier * value
            multiplier *= 100
        strength += multiplier * j # the type is most significant
        t[i].append(strength)
    # sort the array and add to master
    master += sorted(t, key=lambda a: a[2])
        
print(master)

winnings = 0
for i, tri in enumerate(master):
    winnings += tri[1] * (i + 1)
    
print(f'winnings: {winnings}')