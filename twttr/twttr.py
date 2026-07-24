vowels = ["a", "e", "i", "o", "u"]

def main():
    text = input("Type here: ")
    eliminate_vowel(text)

def eliminate_vowel(text):
    result =""
    for vowel in vowels:
        if vowel in text:
            result += vowel
        else:
            print("nothing")
    print(result)

main()
