rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list_game = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#Turno usuario
list_user = list_game[user]
print("Usuario: ")
print(list_user)

#turno computadora
print("Computadora: ")
list_computer = random.choice(list_game)
print(list_computer)

#Condicionales
   #0 roca/ 1 papel/ 2 tijeras

''''''
if list_user == list_computer: 
  print("Empate") 
elif list_user == rock and list_computer == scissors: 
  print("You win!")
elif list_user == rock and list_computer == paper: 
  print("You lose!")
  #papel
elif list_user == paper and list_computer == scissors: 
  print("You lose!")
elif list_user == paper and list_computer == rock: 
  print("You win!")
#tijeras
  print("Empate!")
elif list_user == scissors and list_computer == paper: 
  print("You win!")
elif list_user == scissors and list_computer == rock: 
  print("You lose!")