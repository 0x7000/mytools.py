#!/usr/bin/env python
import urllib.parse
import requests
import re
import wget


def resim_ara(aranan):
    # aranan = input("aranan: ")
    pic = ara(aranan)
    kalan = len(pic)
    for i in pic:
        kalan -= 1
        wget.indir(i, aranan)
        print(kalan)


def ara(obje):
    website = ADRES.format(urllib.parse.quote(obje))
    istek = requests.get(website, headers=AGENT)
    if istek.status_code == 200:
        sonuc = linkara(istek.text)
        if isinstance(sonuc, list):
            return sonuc
        else:
            return False
    else:
        print(istek.status_code)


def linkara(text):
    reg = r"http[s]?:\/\/\S+.jpg"
    liste = re.findall(reg, text)
    return liste


ADRES = "https://www.google.com.tr/search?hl=tr&tbm=isch&q={}"
AGENT = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"}

if __name__ == "__main__":
    resim_ara()
