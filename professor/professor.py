import random


def main():
    level = get_level()
    
    x, y = generate_integer(level)
    print(x, "+", y)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()
