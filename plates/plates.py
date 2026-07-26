def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalidhhh")


def is_valid(plate):
    if 4 >= len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha():
        print("Valid")
    else:
        print("Invalid")

main()
