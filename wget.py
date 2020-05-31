import os


def indir(adres, aranan):
    konum = os.getcwd()
    dosya = adres.split("/")[-1]
    tam_yol = konum+"/pics/"+aranan
    tam_dosya = konum+"/pics/"+aranan+"/"+dosya
    if not os.path.exists(tam_yol):
        os.mkdir(tam_yol)
    komut = "wget --tries=1 --timeout=1 --dns-timeout=1 -q " + adres + " -P " + '"'+tam_yol+'"'
    if not os.path.exists(tam_dosya):
        os.system(komut)
    if os.path.exists(tam_dosya):
        boyut = os.stat(tam_dosya).st_size
        if boyut == 0:
            os.remove(tam_dosya)
    else:
        print("indirilemedi.")
