foods = {"apple": 130,
         "avocado": 50,
         "banana": 110,
         "sweet cherries": 100,
         "kiwifruit": 90,
         "pear": 100
}

def main():
    food = input("Item: ").strip().lower()
    find_nutrition(food, foods)

def find_nutrition(food, foods):
    if food in foods:
        print(f"Callories: {foods[food]}")
    else:
        return False

main()
