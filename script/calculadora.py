print("Buenos días.")
total = input("\n Introduce la cantidad que deseas calcular: ")
personas = input("\n Introduce la cantidad de personas: ")

totalfinal = int(total) / int(personas)

print("\n Cantidad por cada persona a pagar: $" + str(totalfinal))

propina = int(total) * 0.12
print("La propina es del 12%, por lo tanto vas a pagar de propina: $" + str(propina))

