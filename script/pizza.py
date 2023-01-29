# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
S = 15
M = 20
L = 25
total = 0
#SIZE S
if size == "S":
    total = S
    #CONDIMENTO
    if size == "S" and add_pepperoni == "Y":
        total = total + 2
#SIZE M
elif size == "M":
    total = M
    #CONDIMENTO
    if size == "M" and add_pepperoni == "Y":
        total = total + 3
#SIZE L
elif size == "L":
    total = L
    #CONDIMENTO
    if size == "L" and add_pepperoni == "Y":
        total = total + 3
#cheese
if extra_cheese == "Y":
    total +=1

print("Your final bill is: " +str(total))