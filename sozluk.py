import requests
import urllib.parse
import html2text
from bs4 import BeautifulSoup
import re
import random


def ara(obje):
    website = "https://eksisozluk.com/?q={}".format(urllib.parse.quote(obje))
    istek = requests.get(website, headers=AGENT)
    # ilk istek
    if istek.status_code == 200:
        # ilk istek 200 verince sayfa yönlendirmesi
        adres = istek.url + "?p=" + str(random.randint(1, int(sayfabul(istek.text))))
        # print(adres)
        istek2 = requests.get(adres, headers=AGENT)
        sonuclar = mesajlar(istek2.text)
        return sonuclar
    elif istek.status_code == 404:
        return oneri(istek.text)
    else:
        return istek.status_code


def oneri(html):
    sayfa = BeautifulSoup(html, "html.parser")
    p = html2text.HTML2Text()
    p.ignore_links = True
    suggest = sayfa.find_all("a", attrs={"class": "suggested-title"})
    if len(suggest) >= 1:
        return p.handle(str(suggest[0])).strip()
    else:
        return "404?"


def sayfabul(html):
    sayfa = BeautifulSoup(html, "html.parser")
    page = sayfa.find_all("div", attrs={"class": "pager"})
    if len(page) >= 1:
        sonsayfa = str(page[0]).strip()
        regex = r"\"\d+\""
        reg = re.findall(regex, sonsayfa)
        if len(reg) > 1:
            son = str(reg[1]).replace('"', "")
        else:
            son = "1"
        return son
    else:
        return "1"


def mesajlar(html):
    dizi = []
    h = html2text.HTML2Text()
    h.ignore_links = True
    soup = BeautifulSoup(html, "html.parser")
    msg = soup.find_all("div", attrs={"class": "content"})
    for i in msg:
        mesaj = h.handle(str(i)).strip().replace("\n", " ")
        # birden fazla boşluk işaretini tek boşluğa çevir.
        mesaj = re.sub(r"\s+", " ", mesaj)
        dizi.append(mesaj)
    return dizi


AGENT = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"}
