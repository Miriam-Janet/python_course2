# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

BMI = (float(weight)/(float(height) ** 2))
total = round(BMI)
# < menor que  > mayor que
if total < 18.5:
    print("Your BMI is " + str(total) + ",you are underweight")
elif total <= 25:
    print("Your BMI is " + str(total) + ",you have a normal weight")
elif total < 30:
    print("Your BMI is " + str(total) + ",you are slightly overweight")
elif total < 35:
    print("Your BMI is " + str(total) + ",you are obese")
elif total > 35:
    print("Your BMI is " + str(total) + ",you are clinically obese.")