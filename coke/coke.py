def main():
    coins = [5, 10, 25]
    coke_machine(coins)

def coke_machine(coins):
    while True:
        amount_due = 50 
        user_input = input("Amount Due: 50")
        for coin in coins:
            if coin in coins:
                amount_due = 50 - coin
            else:
                print("Amount Due: 50")




main()
