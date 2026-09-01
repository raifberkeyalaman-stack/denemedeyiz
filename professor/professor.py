import random


def main():
    level = get_level()



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            continue

def generate_integer(x, y):
    #x = random.randint(1, level)
    #y = random.randint(1, level)


if __name__ == "__main__":
    main()
