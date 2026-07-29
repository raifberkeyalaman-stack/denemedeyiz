while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        result = round(x / y)
        print((result * 100) +"%")
        break
    except ValueError:
        print("fraction must be a number")

