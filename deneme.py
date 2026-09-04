with open("names.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        print(f"{name} is from {city}")
