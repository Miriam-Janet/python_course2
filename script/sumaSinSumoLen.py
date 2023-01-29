# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
#guarda los numeros en la lista
  student_heights[n] = int(student_heights[n])
  #print(student_heights)
# 🚨 Don't change the code above 👆
#https://www.aluracursos.com/blog/listas-de-python-operaciones-basicas
#Write your code below this row 👇
sumatotal = 0
total = 0
#aqui sumamos
for dato in student_heights:
    sumatotal += dato
    total += 1
#print(sumatotal)
#ahora dividimos
divido = sumatotal/(total)
print(round(divido))