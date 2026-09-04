name = input("Kimsin sen? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

