def main():
    text = input("Input: ")
    text = text.replace(" :)", smiley_face())
    print(text)

def smiley_face(text):
    return str("🙂")

def sad_face(text):
    return str("🙁")

main()
