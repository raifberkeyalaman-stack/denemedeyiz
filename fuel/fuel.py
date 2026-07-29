x = int(input("x is: "))
y = int(input("y is: "))
result = x / y

while True:
    try:
        fraction = int(input("Fraction: {x} / {y}"))
        print((round(result) * 100) +"%")
    except ValueError:

