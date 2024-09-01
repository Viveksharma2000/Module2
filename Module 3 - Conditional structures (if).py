# Module 3 - Exercise 1
zander_limit = 42

# Asking the user for the length of the zander
zander_length = int(input("Please enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if zander_length >= zander_limit:
    print("The zander meets the size limit. You can keep the fish.")
else:
    difference = zander_limit - zander_length
    print(f"The zander does not fulfill the size limit. Please release the fish back into the lake.")

# Exercise 2
# Ask the user to enter the cabin class
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

# Determine the cabin class description using if/elif/else structure
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

# Exercise 3
# Asking the user for their biological gender and hemoglobin value
gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin_value = int(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin_value < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender entered.")

# Exercise 4

year = int(input("Enter a year: "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
