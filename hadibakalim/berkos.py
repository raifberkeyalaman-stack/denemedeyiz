def main():
    height = int(input("Enter a height"))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)



main()
