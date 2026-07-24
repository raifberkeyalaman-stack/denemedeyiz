def main():
    coins = [5, 10, 25]
    money = int(input("Insert coin: "))
    coke_machine(coins)


def coke_machine(coins):
    rest = int()
    if coin in coins:
        for coin in coins:
            rest = 50 - coin
    else:
        print("Amount Due: 50")
    print(rest)

main()


#for coin in coins:
 #       if coin in coins:
  #          rest += 50 - coin
   #     else:
    #        print("Amount Due: 50")
     #   print(rest)
