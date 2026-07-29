result = round(x / y)

while True:
    try:
        fraction = int(input(f"Fraction: ({int(x)} / {int(y)})"))
        print((result * 100) +"%")
        break
    except ValueError:
        print("fraction must be a number")

