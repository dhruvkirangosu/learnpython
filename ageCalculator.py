currentYear = 2021

name = str(input('Please enter your name: '))
birthYear = int(input("Please enter your birth year: "))
height = float(input("Please enter your height: "))

age = currentYear - birthYear

print("Dear {}, your are {} m tall and your age is {}.".format(name, height, age))


