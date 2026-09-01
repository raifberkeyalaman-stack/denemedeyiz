import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1:
                break
        except ValueError:
            continue


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
