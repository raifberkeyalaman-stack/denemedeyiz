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
        print("fraction can not be string")
        if x < 0:
            print("x must be positive")
    except ZeroDivisionError:
        print("y can not be zero")

