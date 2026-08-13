def main ():
    text = input("Greeting: ").strip().lower()

    if text.startswith("hello"):
        print("$0")
    elif text.startswith("h") and text != "hello":
        print("$20")
    else:
        print("$100")

main()
