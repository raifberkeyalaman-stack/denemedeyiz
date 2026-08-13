def main():
    eq = input("Expresion: ")
    x, y, z = eq.split(" ")

    x = int(x)
    z = int(z)

    if y == " + ":
        result = x + Z
    elif y == " - ":
            result = x - Z
    elif y == " / ":
            result = x / Z
    elif y == " * ":
            result = x * Z

    print(f"{result:.1f}")

main()

