x = int(input("x is: "))
y = int(input("y is: "))
result = x / y

while True:
    try:
        fraction = int(input("Fraction: "))
        print((round(result) * 100) +"%")
        break
    except ValueError:
        print("fraction must be a number")

