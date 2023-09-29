"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
length = len(numbers)
midpoint = math.ceil(length/2) - 1
if length % 2 == 0 :
    median = (numbers[midpoint] + numbers[midpoint + 1])/ 2
else:
    median = numbers[midpoint]
#print(f'{numbers}, length = {length}, midpoint = {midpoint}')
print(f'median is {median}')