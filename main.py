#!/usr/bin/env python3
import sozluk
import database


def main():
    dosya = open("tr.list.txt", "r")
    veriler = dosya.readlines()
    dosya.close()
    sayac = len(veriler)
    for i in veriler:
        liste = soru(i)
        sayac -= 1
        if isinstance(liste, list):
            for x in liste:
                print(x)
        else:
            print(liste)
        print(sayac)


def soru(aranan):
    yeniler = sozluk.ara(aranan)  # internetten aranan veriler
    varmi = kontrol(aranan)  # yerel veritabanından alınan veriler
    if varmi:  # yerel veritabanında aranan var ise eski ile yeniler karşılaştırılıyor
        if isinstance(yeniler, list):
            for i in yeniler:
                if i not in ESKILER:
                    database.add(aranan, i)
            del ESKILER[:]  # eskiler işi bitince siliniyor
    else:  # yerel veritabanında yok ise doğrudan kayıt ediliyor
        if isinstance(yeniler, list):
            for i in yeniler:
                database.add(aranan, i)
    liste = sozluk.ara(aranan)  # tüm sonuçlar
    if isinstance(liste, list):
        return liste
    else:
        return yeniler


def kontrol(aranan):
    temp = database.control(aranan)
    if isinstance(temp, list):
        for i in temp:
            ESKILER.append(i)
        return True
    else:
        return False


ESKILER = []

if __name__ == "__main__":
    main()
