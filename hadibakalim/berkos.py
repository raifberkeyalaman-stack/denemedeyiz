while True:
    try:
        number = int(input("Which number?: "))
    except ValueError:
        print("Enter a number not string")
    else:
        print(f"The number is {number}")
        break
