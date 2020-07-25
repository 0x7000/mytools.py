#!/usr/bin/env python
import requests
import html2text


def main():
    req = requests.get("https://www.google.com/search?q=hava+durumu")
    sonuc = req.text
    sicak = html_parse(sonuc)
    print(sicak[0])


def html_parse(data):
    degerler = []
    view = html2text.HTML2Text()
    view.ignorelinks = True
    sonuc = view.handle(data)
    liste = sonuc.splitlines()
    for x in liste:
        if "°" in x:
            degerler.append(x)
    return degerler


if __name__ == "__main__":
    main()