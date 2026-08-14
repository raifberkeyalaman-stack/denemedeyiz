coins = [5, 10, 25]

def main():
    print("Amount Due: 50")
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in coins:
            amount_due = amount_due - insert_coin
        else:
            print(amount_due)
        print("Change Owed:", abs(amount_due))

main()
