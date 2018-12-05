# Author Arthur Dooner
# Advent of Code 2018 Day 2
# Part 2, "Inventory Management Systems"

count_two = []
count_three = []

with open("input.txt", "r") as box_ids:
    for box_id in box_ids:
        visited_elements = set()
        matches_2_elements = False
        matches_3_elements = False
        for element in box_id:
            if (element in visited_elements):
                continue
            temp_count = box_id.count(element)
            visited_elements.add(element)
            if temp_count is 2:
                matches_2_elements = True
            if temp_count is 3:
                matches_3_elements = True
        if matches_2_elements:
            count_two.append(box_id)
        if matches_3_elements:
            count_three.append(box_id)
    print(f'The output checksum is {len(count_two) * len(count_three)}')