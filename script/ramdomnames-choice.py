# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
import random
def selectRandom(names):
  return random.choice(names) #use de ramdom.choice

print(selectRandom(names), "is going to buy the meal today!$")