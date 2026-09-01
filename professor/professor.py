import random


def main():
    level = get_level()
    x, y = generate_integer
    



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            continue

def generate_integer(x, y):
    x = random.randint(1, x)
    y = random.randint(1, y)


if __name__ == "__main__":
    main()
