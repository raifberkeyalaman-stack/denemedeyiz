vowels = ["a", "e", "i", "o", "u"]

def main():
    word = input("Type here: ")
    short_word(word)

def short_word(word):
    result =""
    for letter in word:
        if letter.lower() not in vowels:
           result += letter
    print(result)

main()
