def main():
    camel_case = input("Type here: ")
    convert_snakecase(camel_case)

def convert_snakecase(camel_case):
        for letter in camel_case:
              if letter.isupper():
                    camel_case += "_" + letter.lower()
              else:
                  camel_case += letter
        print(camel_case)

main()
