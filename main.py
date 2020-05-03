#!/usr/bin/env python3
import sozluk
import resim


def main():
    sonuc = sozluk.ara(input("Ara : "))
    if isinstance(sonuc, list):
        for i in sonuc:
            print(i)
    else:
        print(sonuc)


if __name__ == "__main__":
    main()
