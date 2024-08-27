# Exercise Lab - part 2
# Exercise 1
name = input("What is your name? ")
print(f"Hello, {name}!")

# Exercise 2
import math
radius = float(input("What is the radius of the circle? "))
print(f"Area of the circle is {math.pi * radius ** 2:.2f}")

# Exercise 3
rec_length = float(input("What is the length of the rectangle? "))
rec_width = float(input("What is the width of the rectangle? "))
peri_rec = 2 * rec_length + 2 * rec_width
area_rec = rec_length * rec_width
print(f"The perimeter of the rectangle is: {peri_rec:.1f}")
print(f"The area of the rectangle is: {area_rec:.1f}")

# Exercise 4
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
print(f"Sum of 3 numbers is {num1 + num2 + num3}, product {num1 * num2 * num3}, average {(num1 + num2 + num3) / 3:.2f}")

# Exercise 5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
kg_weight = ((talents * 20 + pounds) * 32 + lots) * 0.0133
gr_weight = 1000.0 * (kg_weight - int(kg_weight))
print(f"The weight in modern units:\n{int(kg_weight)} kilograms and {gr_weight:.2f} grams")

# Exercise 6
import random
print(f"First combination of lock code: {random.randint(0, 999):03d}")
four_code = ''.join(str(random.randint(1, 6)) for _ in range(4))
print(f"Second combination of lock code: {four_code}")