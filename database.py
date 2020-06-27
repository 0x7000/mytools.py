import sqlite3 as sql


def add(ask, ans):
    db = sql.connect("sozluk.db")
    db.text_factory = str
    im = db.cursor()
    im.execute('INSERT INTO kelimeler VALUES (?,?)', (ask, ans))
    db.commit()
    db.close()


def control(aranan):  # aranan strip edilmeli.
    dizi = []
    db = sql.connect("sozluk.db")
    db.text_factory = str
    im = db.cursor()
    im.execute("SELECT anlam FROM kelimeler WHERE kelime = ?", [aranan])
    veriler = im.fetchall()
    db.close()
    if veriler:
        for i in veriler:
            dizi.append(i[0])
        return dizi
    else:
        return []
