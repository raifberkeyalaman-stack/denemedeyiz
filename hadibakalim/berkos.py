vowels = ["a", "e", "i", "o", "u"]

def main():
    word = input("Input: ")
    short_words(word)

def short_words(word):
    result =""
    for letter in word:
        if letter.lower() not in vowels:
            result += letter
    print(result)


main()
