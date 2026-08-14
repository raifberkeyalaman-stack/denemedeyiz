def main():
    text = input("camelCase: ")
    convert(text)

def convert(text):
    snake_case = ""
    for letter in text:
        if letter.isupper():
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    print(snake_case)

main()
