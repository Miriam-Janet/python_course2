# π¨ Don't change the code below π
age = input("What is your current age? ")
die = input("When do you think you gona die? ")
# π¨ Don't change the code above π
#Write your code below this line π
new_age = int(die) - int(age)
days = new_age * 365
weeks = new_age * 52
months = new_age * 12
#What is F {} in Python? Image result for print(f {} Also called βformatted string literals,β f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
print(f"You have {days} days, {weeks} weeks, and {months} months left.")