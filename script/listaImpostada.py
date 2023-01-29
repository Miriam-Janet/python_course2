import random
list_name = open('Lista_20_Enero.txt','r')
#print(list_name.readable()) #Esta viendo si lo esta leyendo
lista = list_name.read() # Lee todo el archivo
name = lista.split("\n")
randomName = random.choice(name)
print(randomName)