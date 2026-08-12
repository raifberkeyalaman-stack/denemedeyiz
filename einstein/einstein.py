def main():
    mass = int(input("m: "))
    c = int(300000000)
    print(f"E: {eq(mass, c)}")

def eq(mass, c):
    return mass * c * c

main()
