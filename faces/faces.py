def main():
    text = input("Input: ")
    smiley_face(text)

def smiley_face(text):
    text.replace(" :)", " 🙂")
    print(text)

main()
