import requests
import html2text


def ara():
    istek = requests.get(ADRES, headers=AGENT)
    if istek.status_code == 200:
        h = html2text.HTML2Text()
        print(h.handle(istek.text).strip())
    else:
        print(istek.status_code)


ADRES = "http://checkip.dyndns.org"
AGENT = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"}


if __name__ == "__main__":
    ara()
