#!/usr/bin/env python3
import sozluk
import database


def main():
    dosya = open("sirali.txt", "r")
    veriler = dosya.readlines()
    dosya.close()
    sayac = len(veriler)
    for i in veriler:
        x = i.split(",")[0]
        liste = soru(x.strip())  # aranan strip edilmezse \n eklniyor ve sonuçlar çift çıkıyor
        sayac -= 1
        if isinstance(liste, list):
            for x in liste:
                print(x)
        else:
            print(liste)
        print(sayac)


def soru(aranan):
    yeniler = sozluk.ara(aranan)  # internetten aranan veriler
    temp = database.control(aranan)  # yerel veritabanından alınan veriler
    if isinstance(yeniler, list):
        for i in yeniler:
            if i not in temp:
                database.add(aranan, i)
    liste = database.control(aranan)  # tüm sonuçlar
    return liste


#  84095 son işlem satırı
if __name__ == "__main__":
    main()
