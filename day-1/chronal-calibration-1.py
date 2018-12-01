# Author Arthur Dooner
# Advent of Code 2018 Day 1
# Part 1, "Chronal Calibration"

current_frequency = 0

with open("input.txt", "r") as frequency_changes:
    for line in frequency_changes:
        if line[0] is '+':
            current_frequency += int(line[1:])
        elif line[0] is '-':
            current_frequency -= int(line[1:])
            
print(f'The resulting frequency, the answer to your version of Chronal Calibration Part 1, is {current_frequency}')