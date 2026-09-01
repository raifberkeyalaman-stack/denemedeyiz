import random


def main():
    




def get_level(level):
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            continue

def generate_integer(level):
    number = random.randint(1, level)


if __name__ == "__main__":
    main()
