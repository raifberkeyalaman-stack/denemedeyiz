def main():
    m = int(input("How many kilo?: "))
    c = 300000000
    print("The energy is", formula(m, c))

def formula(m, c):
    return  m * c * c

main()
