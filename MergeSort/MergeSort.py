import os
import re

"""MergeSort.py"""
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    merge = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merge.append(left[left_index])
            left_index += 1
        else:
            merge.append(right[right_index])
            right_index += 1

    merge += left[left_index:]
    merge += right[right_index:]

    return merge

def is_comma_separated_numbers(str):
    regex = r"^\d+(,\d+)*$"
    return re.fullmatch(regex, str)

file_path = "./arrays.csv"
if not os.path.exists(file_path):
    print(f"File {file_path} is missing\n")
    exit()

with open(file_path, encoding='UTF-8') as file:
    line = file.readline().strip()
    while line:
        if not is_comma_separated_numbers(line):
            print(f"input data format is wrong {line}\n")
            line = file.readline().strip()
            continue

        numbers = [int(num) for num in line.split(",")]
        print(numbers)

        sorted_numbers = merge_sort(numbers)
        print(sorted_numbers)
        print()

        line = file.readline().strip()

