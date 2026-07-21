def main():
    text = str(input("Type here: "))
    text = text.replace(":)", smiley_face())
    text = text.replace(":(", sad_face())
    print(text)

def smiley_face():
    return str("🙂")

def sad_face():
    return str("🙁")

main()

