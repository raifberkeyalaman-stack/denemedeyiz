def main():
    time = int(input("The time is: "))
    print(convert(time))
    if (7 < time <=8):
        print("breakfast time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
