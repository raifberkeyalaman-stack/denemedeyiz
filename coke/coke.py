coins = [5, 10, 25]
price = 50
kalan_miktar = 0

def main():
    first_question = int(input("Insert a coin: "))
    coke_machine(first_question, kalan_miktar)


def coke_machine(first_question, kalan_miktar):
    while price > 0:
        if first_question in coins:
            price -= kalan_miktar
            print("Amount Duo:", price)
        else:
            print(f"Amount Duo: {price}")
        continue
    print(kalan_miktar)

main()

