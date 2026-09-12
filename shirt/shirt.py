import sys
import os
from PIL import Image, ImageOps

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

    if extension2 not in [".jpg", ".png", ".jpeg"]:
        sys.exit("Invalid output")

    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, shirt)
        image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
