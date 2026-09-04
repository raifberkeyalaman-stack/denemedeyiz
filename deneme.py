name = input("Kimsin sen? ")

with open("names.txt", "r") as file:
    file.write(f"{name}\n")

