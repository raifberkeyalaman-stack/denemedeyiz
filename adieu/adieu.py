import inflect

p = inflect.engine()

names = []

while True:
    try:
        print("Name: ", end="")
        name = input()
        names.append(name)

    except EOFError:
        print()
        break

result = p.join(names, conj="and", final_sep=",")
print(f"Adieu, adieu, to {result}")
