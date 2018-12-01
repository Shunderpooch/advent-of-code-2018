# Author Arthur Dooner
# Advent of Code 2018 Day 1
# Part 2, "Chronal Calibration"

frequency_pattern = []

with open("input.txt", "r") as frequency_changes:
    frequency_pattern = frequency_changes.readlines()
    
frequencies_reached = set()
current_frequency = 0
frequency_index = 0
while current_frequency not in frequencies_reached:
    frequencies_reached.add(current_frequency)
    frequency_change = frequency_pattern[frequency_index % len(frequency_pattern)]
    if frequency_change[0] is '+':
        current_frequency += int(frequency_change[1:])
    elif frequency_change[0] is '-':
        current_frequency -= int(frequency_change[1:])
    frequency_index += 1
    #print(frequencies_reached)


#print(frequencies_reached)
print(f'The resulting frequency, the answer to your version of Chronal Calibration Part 2, is {current_frequency}')