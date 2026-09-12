import sys
import csv


def main():
    if len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        with open("before.csv", newline="") as before, :
            reader = csv.DictReader(before)
            for row in reader:
                print(row)

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
