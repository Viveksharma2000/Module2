# Module 6 - Exercise 1
import random

num_dice = int(input("How many dice to roll? "))

total_sum = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"The sum of the {num_dice} dice rolls is: {total_sum}")

# Exercise 2
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)

# Exercise 3
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

user_input = int(input("Enter an integer: "))

if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

# Exercise 4
cities = []

for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("\nThe cities you entered are:")
for city in cities:
    print(city)
