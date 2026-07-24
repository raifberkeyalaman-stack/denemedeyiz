coins = [5, 10, 25]
price = 50
kalan_miktar = int()

def main():
    first_question = int(input("Insert a coin: "))
    coke_machine(first_question, kalan_miktar)



def coke_machine(first_question, kalan_miktar):
    while kalan_miktar > 0:
        if first_question in coins:
            kalan_miktar += price - first_question
        else:
            print(f"Amount Duo: {price}")
        continue
    print(kalan_miktar)


main()

