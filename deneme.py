name = input("Kimsin sen? ")

file = open("names.txt", "a")
file.write(name)
file.close()

