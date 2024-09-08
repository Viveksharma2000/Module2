# Module 6 - Exercise 1
import random
import math
def dice_roll():
    return random.randint(1,6)

while True:
    dice = dice_roll()

    print(f"Dice's eyes are: {dice}")
    if dice == 6:
        break

# Exercise 2
def dice_roll_side (num):
    return random.randint(1,num)

num = int(input("How many sides in your dice? "))
while True:
    dice = dice_roll_side(num)
    print(f"Dice's sides are: {dice}")
    if dice == num:
        break

# Exercise 3
def gallons_to_litres(gallon):
    return 3.7854 * gallon

while True:
    user_gallon = float (input("How many gallons to convert? "))
    if user_gallon < 0:
        break
    print(f"{user_gallon} gallons are {gallons_to_litres(user_gallon):.1f} litres. ")

# Exercise 4
def sum(num_list):
    total_sum = 0
    for i in num_list:
        #total_sum = total_sum + i
        total_sum += i
    return total_sum

ex_list = []
for number in range(10):
    ex_list.append(random.randint(1,10))
print(f"The list of numbers is: ")

for i in range (len(ex_list)):
    print(ex_list[i], end= " ")

print(f"\nThe sum of all items in the list is: {sum(ex_list)}")

# Exercise 5
def make_even (num_list):
    result = []
    for i in range (len(num_list)):
        if num_list[i] % 2 == 0:
            result.append(num_list[i])
    return result

def print_list (message, num_list):
    print(message, end= ": ")
    for i in range (len(num_list)):
        print(num_list[i], end= " ")

example_list = []
for n in range (10):
    example_list.append(random.randint(1,99))
print_list ("Original List", example_list )
new_list = make_even(example_list)
print_list("\nOnly even number list", new_list)

# Exercise 6
def pizza_efficiency(d, price):
    return price/math.pi * (d / 200. ) ** 2

p1_diameter = float(input("What is the diameter of the 1st pizza (in cm)? "))
p1_price = float(input("What is the price of the 1st pizza (in euros)? "))
p2_diameter = float(input("What is the diameter of the 2nd pizza (in cm)? "))
p2_price = float(input("What is the price of the 2nd pizza (in euros)? "))

if pizza_efficiency(p1_diameter, p1_price) < pizza_efficiency(p2_diameter, p2_price):
    print("The first pizza is a better choice! Grab it")
else:
    print("The second pizza is a better choice! Grab it")