coins = [5, 10, 25]

def main():
    print("Amount Due: 50")
    while True:
        insert_coin = int(input("Insert Coin: "))
        for coin in coins:
            amount_due = insert_coin - coin


main()
