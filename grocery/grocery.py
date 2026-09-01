grocery_list ={}
while True:
    try:
        food = input().upper()
        if food in grocery_list:
            grocery_list[food] += 1
        else:
            grocery_list[food] = 1
    except EOFError:
        break

for food in sorted(grocery_list):
    print(grocery_list[food], food)

