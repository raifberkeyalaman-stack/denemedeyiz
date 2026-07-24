vowels = ["A", "E", "I", "O", "U"]

def main():
    text = input("Type here: ")
    eliminate_vowel(text)

def eliminate_vowel(text):
    result =""
    for vowel in text:
        if vowel in text:
            result += ""
        else:
            print("nothing")
        print(result)


main()
