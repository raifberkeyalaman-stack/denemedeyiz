def main():
    text = str(input("Input: ").replace(" :)", smiley_face()))
    print(text)

def smiley_face(text):
    return str("🙂")

def sad_face(text):
    return str("🙁")

main()
