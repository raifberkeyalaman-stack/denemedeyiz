names = []

with open("names.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")

for name in sorted(names):
    print(f"{name} is from {city}")
