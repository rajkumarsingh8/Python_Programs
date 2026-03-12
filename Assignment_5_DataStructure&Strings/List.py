# list of numbers from 1 to 10.
original_list = [1,2,3,4,5,6,7,8,9,10]

# first five elements from the list.
firstFiveElements = original_list[0:5]

# Reverses of the extracted elements.
reverseFiveElements = firstFiveElements[::-1]

print(f"Original list: {original_list}")
print(f"Extracted first five elements: {firstFiveElements}")
print(f"Reversed extracted elements: {reverseFiveElements}")