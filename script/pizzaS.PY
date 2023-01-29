print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small = 15
medium = 20
large = 25

if size == 's':
    bill = small

if add_pepperoni == "y":
    bill += 2
if extra_cheese == 'y':
    bill += 3
    print(f"your total bill is {bill}")
elif size == 'm':
    bill = medium
if add_pepperoni == "y":
    bill += 2
if extra_cheese == 'y':
    bill += 3
    print(f"your total bill is {bill}")
elif size == 'l':
    bill = large
if add_pepperoni == "y":
    bill += 2
if extra_cheese == 'y':
    bill += 3
    print(f"your total bill is {bill}")

else:
    print('Please select your pizza first')