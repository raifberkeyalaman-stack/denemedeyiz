def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalidhhh")


def is_valid(plate):
    if 4 >= len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha():
        print("Valid")
    elif len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha() and plate[2].isdecimal():
        print("Valid")
    else:
        print("Invalid")

main()
