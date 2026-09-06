people = []

with open("names.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        person = {"name": name, "city": city}
        people.append(person)

def get_name(person):
    return person["name"]

for person in sorted(people, key=get_name):
    print(f"{person['name']} is from {person['city']}")


