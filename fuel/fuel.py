while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        percantage = round(x / y * 100)
        print(str(percantage) + "%")
    except ValueError:
        print("fraction can not be string")
    except ZeroDivisionError:
        print("y can not be zero")
    if x < 0 or y < 0 or x > y:
        break
    print("x can not be negative")


