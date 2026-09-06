import sys
import csv
from tabulate import tabulate

menu =[]

def main():
    if len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            menu = list(reader)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
