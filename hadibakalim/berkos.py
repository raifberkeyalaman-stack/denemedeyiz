def main():
    liste = []

    while True:
        ekle = input("Yaz bakalim: ")
        if ekle == "undo":
            geri_aldim = liste.pop()
            print(f"neyi geri aldim: {geri_aldim}")
        else:
            liste.append(ekle)
        print(liste)

main()
