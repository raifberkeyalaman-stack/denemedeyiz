def main():
    coins = [5, 10, 25]
    coke_machine(coins)


def coke_machine(coins):
    rest = []
    for coin in coins:
        if coin in coins:
            rest = 50 - coins



main()
