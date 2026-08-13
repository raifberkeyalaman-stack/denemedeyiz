def main ():
    text = input("Greeting: ").strip().lower()

    if text == "hello":
        print("$0")
    elif text.startswith("h") and not text.startswith("hello"):
        print("$20")
    else:
        print("$100")

main()
