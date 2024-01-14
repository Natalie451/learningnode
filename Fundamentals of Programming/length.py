import math
import random

fruit = "banana"
print(f"Count the number of characters in the string: {fruit} is: ")
print(len(fruit))
print("")

fruits = ["banana", "apple", "orange"]
print("The number of elements in the list is: ")
print(len(fruits))
print("")

# Add 2 lists together
boy_toys = ["car", "truck", "lego"]
girl_toys = ["doll", "stuffed animal", "dress up"]
print("Add 2 lists together: ")
all_toys = boy_toys + girl_toys
print(f"The length of the first list is {len(boy_toys)} and the length of second list is {len(girl_toys)}. When the lists are added together, the total length of the new list is {len(all_toys)}")
print("")

# Position
def get_number_suffix(number):
    if number == 1:
        return "st"
    elif number == 2:
        return "nd"
    elif number == 3:
        return "rd"
    else:
        return "th"
    

word = "Edith-Samuel Sbenghe"
random_number = math.floor(random.random() * len(word))
random_number += 1
number_suffix = get_number_suffix(random_number)
print(f"The {random_number}{number_suffix} character in the word {word} is {word[random_number-1]}")