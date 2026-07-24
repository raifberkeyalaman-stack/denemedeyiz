def main():
    coins = [5, 10, 25]
    coke_machine(coins)

def coke_machine(coins):
    while True:
        user_input = input("Amount Due: 50")
        for coin in coins:
            if coin in coins:
                print(f"Amount Due: 50 - {coin}")
            else:
                print("Amount Due: 50")




main()
