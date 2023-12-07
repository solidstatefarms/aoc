#!/usr/bin/env python3
# Advent of Code day 6 part 2
# PFO
filename = "races.txt"

with open(filename) as f:
    fileArray = f.readlines()
    # split() with no arguments will split on whitespace
    times = fileArray[0].strip().split(':')[1].strip().split()
    distances = fileArray[1].strip().split(':')[1].strip().split()

# concatenate the values in the arrays
bigTime = ''
bigDistance = ''
for time, distance in zip(times, distances):
    bigTime += time
    bigDistance += distance
    
times = [bigTime]
distances = [bigDistance]

print("times")
print(bigTime)
print("distances")
print(bigDistance)

ways = 0
t = int(bigTime)
d = int(bigDistance)
print(f"race time {t}")
for speed in range(1, t):
    distance = speed * (t - speed)
    if distance > d:
        ways += 1
        #print(f"can win with speed {speed}")
    
print(f"ways to win: {ways}")