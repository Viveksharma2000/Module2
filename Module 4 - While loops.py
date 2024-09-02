# Module 4 - Exercise 1

number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

# Exercise 2

while True:
    inches = float(input("Enter inches (negative value to stop): "))
    if inches < 0:
        print("Program ends")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:.2f} centimeters")

# Exercise 3

largest = 0
smallest = 0

number = input("Enter your number: ")
if number != "":
    smallest = largest = int(number)
    while number != "":
        numberAsInt = int(number)
        if numberAsInt < smallest:
            smallest = numberAsInt
        elif numberAsInt > largest:
            largest = numberAsInt
        number = input("Enter your number: ")
    else:
        print(largest, smallest)

# Exercise 4

import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))
    if guess < number:
        print("Your guess is too low!")
    elif guess > number:
        print("Your guess is too high!")
    else:
        print("Correct!")
        break

# Exercise 5

username = "python"
password = "rules"
num_try = 5
while num_try > 0:
    name = input("Enter your username; ")
    pas = input("Enter your password: ")
    if name == username and pas == password:
        print("Welcome")
        break

    num_try = num_try - 1 #num_try -=1
else:
    print("Access denied")

# Exercise 6

import random
import math

random_points = int(input("How many random points should be generated? "))
inside_points = 0
i = 0

while i < random_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_points += 1
    i += 1

pi = 4 * inside_points / random_points
print(f"Pi estimation is {pi}, the difference with math.pi is: {math.pi - pi}")
