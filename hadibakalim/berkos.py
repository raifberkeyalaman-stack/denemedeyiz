def main():
    rows = 5
    num = 1

    for i in range(1, rows + 4):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

main()
