def main():
    coins = [5, 10, 25]
    coke_machine(coins)


def coke_machine(coins):
    rest = int()
    money = int(input("Insert coin: "))
    for coin in coins:
        if coin in coins:
            rest += 50 - coin
        else:
            print("Amount Due: 50")
        print(rest)

main()
