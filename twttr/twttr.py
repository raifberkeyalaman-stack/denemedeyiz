vowels = ["A", "E", "I", "O", "U"]
result =""
def main():
    text = input("Type here: ")
    eliminate_vowel(text)

def eliminate_vowel(text):

    if vowel in text:
        result += vowel
    else:
        print("nothing")
    print(result)


main()
