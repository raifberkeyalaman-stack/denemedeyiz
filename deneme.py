name = input("Kimsin sen? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

