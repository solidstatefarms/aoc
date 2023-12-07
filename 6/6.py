#!/usr/bin/env python3
# Advent of Code day 6
# PFO
filename = "races.txt"

with open(filename) as f:
    fileArray = f.readlines()
    # split() with no arguments will split on whitespace
    times = fileArray[0].strip().split(':')[1].strip().split()
    distances = fileArray[1].strip().split(':')[1].strip().split()

print("times:")
print(times)
print("distances:")
print(distances)

result = 1
for i in range(len(times)):
    ways = 0
    t = int(times[i])
    d = int(distances[i])
    print(f"race time {t}")
    for speed in range(1, t):
        distance = speed * (t - speed)
        if distance > d:
            ways += 1
            print(f"can win with speed {speed}")
    result *= ways        
    
print(f"result is: {result}")