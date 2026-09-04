names = []

with open("names.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        names.append(f"{name} is from {city}")

for name in sorted(names):
    print(name)
