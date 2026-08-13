def main():
    text = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    if text == "forty two" or text == "42" or text == "forty-two":
        print("yes")
    else:
        print("no")

main()

