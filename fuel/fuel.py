while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        percantage = round(x / y * 100)
        print(str(percantage) + "%")
        break
    except ValueError:
        print("fraction must be a number")
    except 

