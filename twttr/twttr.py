vowels = ["a", "e", "i", "o", "u"]

def main():
    text = input("Input: ")
    kelime = ""
    for vowel in vowels:
        if vowel not in text:
            kelime += text
        else:
            kelime = text.replace(vowel, "")
    print(kelime)



main()
