vowels = ["A", "E", "I", "O", "U"]

def main():
    text = input("Type here: ")
    eliminate_vowel(text)

def eliminate_vowel(text, vowel):
    result =""
    if vowel in text:
        result += vowel
    else:
        print("nothing")
    print(result)


main()
