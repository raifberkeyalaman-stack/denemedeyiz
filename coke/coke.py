coins = [5, 10, 25]

def main():
    coke_machine()

def coke_machine():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert coin: "))
        if coin in coins:
            amount_due -= coin
        else:
            print("Amount Due:", amount_due)
        print("Change Owed:", abs(amount_due))


main()
