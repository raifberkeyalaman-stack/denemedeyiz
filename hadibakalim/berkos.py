def main():
    n = int(input("how many times: "))
    print(meow(n))

def meow(n):
    while True:
        if n > 0:
            break
    for i in range(n):
        print("meow")

main()
