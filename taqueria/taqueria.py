menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while True:
      try:
        food = input("Food: ")
        if food in menu:
            print(f"${menu[food]}")
        else:
            print("Item is not in the menu")
      except EOFError:
          print("stop")
          break




