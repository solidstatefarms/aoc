#!/usr/bin/env python3
# Advent of Code day 7
# PFO
import re
import copy
filename = "hands.txt"
hands = []
with open(filename) as f:
    for line in f:
        hands.append([a for a in line.strip().split()])
highCard = copy.deepcopy(hands)

# find five of a kind
fiveKind = []
for hand, bid in hands:
    notFiveKind = False
    for card in list(hand[1:]):
        if not hand[0] == card:
            notFiveKind = True
    if not notFiveKind:
        print('found five of a kind')
        fiveKind.append([hand, int(bid)])
        highCard.remove([hand, bid])
print(fiveKind)

# find four of a kind
fourKind = []
for hand, bid in hands:
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if count == 4:
            print('found four of a kind')
            fourKind.append([hand, int(bid)])
            highCard.remove([hand, bid])
            break
print(fourKind)

# find full house and three of a kind
fullHouse = []
threeKind = []
for hand, bid in hands:
    foundThree = False
    foundTwo = False
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if count == 3:
            print('found three of a kind')
            foundThree = True
        if count == 2:
            print('found two of a kind')
            foundTwo = True
    if foundThree and foundTwo:
        fullHouse.append([hand, int(bid)])
        highCard.remove([hand, bid])
    elif foundThree:
        threeKind.append([hand, int(bid)])
        highCard.remove([hand, bid])
print(fullHouse)
print(threeKind)

# find two pair and one pair
twoPair = []
onePair = []
for hand, bid in hands:
    foundTwo = 0
    for card in list(hand):
        rx = re.compile(card)
        count = len(rx.findall(hand))
        if count > 2:
            foundTwo = 0
            break
        if count == 2:
            print('found two of a kind')
            foundTwo += 1
    if foundTwo == 4:
        twoPair.append([hand, int(bid)])
        highCard.remove([hand, bid])
    elif foundTwo == 2:
        onePair.append([hand, int(bid)])
        highCard.remove([hand, bid])
print(twoPair)
print(onePair)

# fix up highCard to make the bid an int
for i, handBid in enumerate(highCard):
    highCard[i] = [handBid[0], int(handBid[1])]
print(highCard)

# compute a strength value for each hand
# expand each char to two digits, and also the type
# and then append to create a base 10 integer
# X1,234,567,890
# append this to each hand and bid array as a third element
nums = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A':14}
master = []
for j, t in enumerate([highCard, onePair, twoPair, threeKind, fullHouse, fourKind, fiveKind]):
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