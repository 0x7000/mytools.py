#!/usr/bin/env python
import os


def main():
    konum = os.getcwd()
    klasor = "d 1"
    dosya = ADRES.split("/")[-1]
    tam_yol = konum+"/"+klasor
    tam_dosya = konum+"/"+klasor+"/"+dosya
    if not os.path.exists(tam_yol):
        os.mkdir(klasor)
    komut = "wget -q " + ADRES + " -P " + '"'+tam_yol+'"'
    if not os.path.exists(tam_dosya):
        os.system(komut)
    if os.path.exists(tam_dosya):
        boyut = os.stat(tam_dosya).st_size
        if boyut == 0:
            os.remove(tam_dosya)
        print(boyut)
    else:
        print("dosya yok")


ADRES = "https://n11scdn.akamaized.net/a1/450/ev-yasam/hesap-makinesi/casio-fx-82ms-bilimsel-fonksiyonlu-hesap-makinesi__0340777259406790.jpg"

if __name__ == '__main__':
    main()
