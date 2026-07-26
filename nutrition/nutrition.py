foods ={"apple": 130 }

def main():
    item = input("Item: ")
    find_nutrition(foods)


def find_nutrition(food):

    if food in foods.keys():
        print("key", "value")

