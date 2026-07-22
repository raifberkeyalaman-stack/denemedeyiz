def main():
    time = input("The time is: ")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
