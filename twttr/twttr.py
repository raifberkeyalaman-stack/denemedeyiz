vowels = ["a", "e", "i", "o", "u"]

def main():
    text = input("Input: ")
    without_vowel(text)


def without_vowel(text):
    kelime = ""
    for vowel in text:
        if vowel not in text:
            kelime += text
        else:
            kelime = text.replace(vowel, "")
    print(kelime)


main()
