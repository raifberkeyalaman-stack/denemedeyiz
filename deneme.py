names = []

with open("names.txt") as file:
    for line in file:
        names.append(line)

for line in sorted(names):
    print("Hello", line.rstrip())
