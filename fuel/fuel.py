x = int(x)
y = int(y)
result = x / y

while True:
    try:
        fraction = int(input("Fraction: {result}"))
        print((round(result) * 100) +"%")
    except ValueError:

