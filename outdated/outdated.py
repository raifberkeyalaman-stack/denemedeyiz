months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ")
            month, day, year = date.split("/")
            day = int(day)
            month = int(month)
            year = int(year)

        except ValueError:
            try:
                if "," not in date:
                    continue
                    
                month, day, year = date.split(" ")
                month = months.index(month) + 1
                day = int(day.replace(",", ""))
                year = int(year)

            except ValueError:
                continue


        if day < 1 or day > 31:
            continue
        if month < 1 or month > 12:
            continue
        print(f"{year}-{month:02}-{day:02}")
        break

main()


