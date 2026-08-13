def main():
    text = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    if text == "forty two" or text == "42":
        print("yes")
    else:
        print("no")

main()

