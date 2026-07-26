foods = {"apple": 130,
         "avocado": 50,
         "banana": 110}

def main():
    food = input("Item: ").lower()
    find_nutrition(food, foods)


def find_nutrition(food, foods):

    if food in foods:
        print(f"Calories: {foods[food]}")
    else:
        print("nothing")
main()


