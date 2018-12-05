# Author Arthur Dooner
# Advent of Code 2018 Day 2
# Part 2, "Inventory Management Systems"

count_two = []
count_three = []
count_all = []
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
        if matches_2_elements or matches_3_elements:
            count_all.append(box_id)
    result = None
    element = count_all.pop()
    while result is None:
        for another_element in count_all:
            if sum(char1 != char2 for char1, char2 in zip(element, another_element)) is 1:
                result = [element, another_element]
        element = count_all.pop()
    counter = 0
    index = None
    for char1, char2 in zip(result[0], result[1]):
        if char1 != char2:
            index = counter
        counter += 1
    print(f'The output of part 2, the string parts in common that are only one letter away, is {result[0][:index]}{result[0][(index + 1):]}')