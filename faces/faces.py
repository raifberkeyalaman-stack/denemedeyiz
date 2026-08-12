def main():
    text = input("Input: ")
    smiley_face(text)
    sad_face(text)

def smiley_face(text):
    print(text.replace(" :)", " 🙂"))

def sad_face(text):
    print(text.replace(" :(", " 🙁"))

main()
