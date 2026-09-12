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

    if not sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png"):
        sys.exit("Invalid output")

    try:
        with Image.open(sys.argv[1]) as before1:
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")

            image = ImageOps.fit(image, shirt.size)

            image.paste(sys.argv[1], shirt)

            image.save("after.jpg")



    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
