print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm: "))
ticket = 0
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age: "))
#Menos a 12
    if age < 12:
        ticket += 5
        print("Child ticket: " + str(ticket))
# entre 12 a 18
    elif age >= 12 and age <= 18:
        ticket += 7
        print("Teenager tickYet: " + str(ticket))

    elif age >= 19 and age <= 44:
        ticket += 12
        print("Adult ticket: " + str(ticket))

    elif age >= 45 and age <= 55:
        ticket += 0
        print("Your ride is free " + str(ticket))
 #photo
photo = input("Do you want a photo taken: Y or N ")

if photo == "Y":
    ticket += 3
    print("Your final bill is " + str(ticket))
elif photo == "N":
    print("Your final bill is " + str(ticket))
##################
else:
    print("You can´t ride")


