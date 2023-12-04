#!/usr/bin/env python3
# Advent of Code day 1 part 2
# PFO
import re

filename = "calibration_values.txt"

total = 0
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(filename) as f:
    for line in f:
        digit1_found = False
        digit2_found = False
        line = line.strip()
        print(f'processing: {line}')
        
        # find earliest word or number
        for a in range(len(line)):
            if digit1_found:
                break
            print(line[:a+1])
            # check if number is there, in which case we can skip
            try:
                digit1 = int(line[a])
                print(f'found start number: {digit1}')
                digit1_found = True
            except:
                pass
            # check if number word is in substring
            for i, word in enumerate(words):
                rx = re.compile(word)
                match = rx.search(line[:a+1])
                if not type(None) == type(match):
                    # the word has been found
                    digit1 = i
                    print(f'found start word: {digit1}')
                    digit1_found = True
                
        # find last word or number
        for a in range(len(line), 0, -1):
            if digit2_found:
                break
            print(line[a-1:])
            # check if number is there, in which case we can skip
            try:
                digit2 = int(line[a-1])
                print(f'found end number: {digit2}')
                digit2_found = True
            except:
                pass
            # check if number word is in substring
            for i, word in enumerate(words):
                rx = re.compile(word)
                match = rx.search(line[a-1:])
                if not type(None) == type(match):
                    # the word has been found
                    digit2 = i
                    print(f'found end word: {digit2}')
                    digit2_found = True

        number = digit1 * 10 + digit2
        total += number
print(f'the total is {total}')


