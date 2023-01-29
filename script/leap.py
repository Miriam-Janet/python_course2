year = (int(input("Which year do u want to know?\n")))

#Solution 3 #Update + Extra #This Code checks if a year is leap or normal and prints the result, then it prints the explanation why it is leap or normal

if year % 4 == 0 and year % 100 > 0 or year % 100 == 0 and year % 400 == 0:

    print("Leap year.")

    if year % 4 == 0 and year % 100 > 0:

      print(f"Because {year} is cleanly divisible by 4")

      print(f"And {year} is not cleanly divisible by 100")

    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:

      print(f"Because {year} is cleanly divisible by 4")

      print(f"And {year} is cleanly divisible by 100")

      print(f"And {year} is cleanly divisible by 400")

else:

    print("Normal year.")

    print(f"Because {year} is NOT divisible by 4")