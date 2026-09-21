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


    today = date.today()
    days = (today - birth).days
    minutes = days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    print(words.capitalize(), "minutes")


if __name__ == "__main__":
    main()
