from datetime import date
import sys
import inflect


def main():
    birth_date = input("Date of birth: ")
    try:
        year, month, day = map(int, birth_date.split("-"))
        birth = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")


...


if __name__ == "__main__":
    main()
