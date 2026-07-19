def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

    y = int(input("What is y? "))
    print("y tripled is", triple(y))

def square(n):
    return n * n

def triple(m):
    return m * m * m

main()
