vowels = ["a", "e", "i", "o", "u"]

def main():
    text = input("Input: ").lower().strip()
    kelime=""
    for letter in text:
        if letter not in vowels:
            kelime += letter
        else:
            kelime = text.replace(letter, "")
    print(kelime, end=" ")

main()
