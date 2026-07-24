coins = [5, 10, 25]
price = 50

def main():
    first_question = int(input("Insert a coin: "))
    coke_machine()



def coke_machine(first_question, kalan_miktar):
    kalan_miktar = int()
    if first_question in coins:
        kalan_miktar += price - first_question
    else:
        print(f"Amount Duo: {price}")
    print(kalan_miktar)




main()

