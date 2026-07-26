foods ={"apple": 130}

def main():
    food = input("Item: ")
    find_nutrition(food, foods)


def find_nutrition(food, foods):

    if food in foods:
        print(food, foods[food])
    else:
        print("nothing")

