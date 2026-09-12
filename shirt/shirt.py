import sys
import csv
import os



def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    extension1 = os.path.splitext(file1)[1]
    extension2= os.path.splitext(file2)[1]

    if extension1 != extension2:
        sys.exit("Input and output have different extensions")

    if 


