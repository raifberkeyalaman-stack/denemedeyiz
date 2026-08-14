vowels = ["a", "e", "i", "o", "u"]

def main():
    text = input("Input: ")
    kelime=""
    for letter in text:
        if letter.lower() not in vowels:
            kelime += letter
    print(kelime, end=" ")

main()
