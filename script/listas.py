import random
#http://runest.ing.puc.cl/list.html
list_name = ['Fernanda', 'Melisa del Carmen',  'José', 'Miriam Janet', 'Natalia', 'Tamara' , 'Jasive' , 'Gabriel', 'Jonathan Palacios (Emmanuel)', 'Kenia', 'Rodrigo','Luis', 'Yamil','Cinthia Melisa', 'Miguel']
            #def is the keyword for defining a function.
def selectRandom(list_name):
  return random.choice(list_name)

print("The name selected is: ", selectRandom(list_name))