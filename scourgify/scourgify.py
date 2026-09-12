import sys
import csv


def main():
    if len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


    with open("before.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)



main()
