import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayınevi,tür,baskı):

        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı

    def __str__(self):

        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)


class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitapları_goster(self):

        sorgu =  "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor.....")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])

            print(kitap)
    def kitap_ekle(self,kitap):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def baskı_yükselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            baskı = kitaplar[0][4]

            baskı += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baskı,isim))

            self.baglanti.commit()

print("""
*****************************************
Kütüphane Programına hoşgeldiniz.

İşlemler;

1.Kitapları Göster
2.Kitap Sorgulama
3.Kitap Ekle
4.Kitap Sil
5.Baskı Yükselt


Çıkış için 'q' ya basınız.
*****************************************""")
kütüphane = Kütüphane()

while True:
    işlem = input("yapacağınız işlem : ")
    if işlem == "q":
        print("program kapanıyor...")
        time.sleep(0.4)
        print("Yine bekleriz...")
        break
    elif (işlem == "1"):
        kütüphane.kitapları_goster()
    elif (işlem == "2"):
        isim = input("hangi kitabı istiyorsunuz: ")
        print("Kitap sorgulanıyor....")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))
        print("Kitap ekleniyor....")
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")
    elif (işlem == "4"):
        isim = input("silmek istediğiniz kitabın ismi: ")
        cevap = input("kitabı silmek istediğinize emin misiniz? (e/h)")
        if (cevap == "e"):
            kütüphane.kitap_sil(isim)
            print("Kitap siliniyor...")
            time.sleep(2)
            print("Kitap silindi")
        else:
            continue
    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz:")
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        print("Baskı yükseltildi")
    else:
        print("geçersiz işlem")