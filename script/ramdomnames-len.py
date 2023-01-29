import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]
print(f"{random_index} is going to buy the meal today!")

'''billname = random.randint(0, (len(names) - 1))
print(f"{names[billname]} is going to buy the meal today!")
'''

"""The randint(start, end) function accepts two arguments and returns an integer value between the function's starting and ending points.

The following example prints a 4 digit random number between 1000 to 9999:

import random

print(random.randint(1000,9999))
The output of the above example will look like this:

7283"""
