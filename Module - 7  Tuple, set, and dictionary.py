# Exercise 1
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of the month (1-12): "))

if month in [12, 1, 2]:
    season = seasons[0]  # Winter
elif month in [3, 4, 5]:
    season = seasons[1]  # Spring
elif month in [6, 7, 8]:
    season = seasons[2]  # Summer
elif month in [9, 10, 11]:
    season = seasons[3]  # Autumn
else:
    season = "Invalid month number. Please enter a number between 1 and 12."

print(f"The season is: {season}")

# Exercise 2
names = set()

while True:
    name = input("Enter a name (or press Enter to stop): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nList of names entered:")
for name in names:
    print(name)

# Exercise 3
airports = {}

while True:
    print("\nChoose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        icao_code = input("Enter ICAO code of the airport: ").upper()
        name = input("Enter the name of the airport: ")

        airports[icao_code] = name
        print(f"Airport {name} with ICAO code {icao_code} added.")

    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport: ").upper()


        if icao_code in airports:
            print(f"The airport name is: {airports[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

