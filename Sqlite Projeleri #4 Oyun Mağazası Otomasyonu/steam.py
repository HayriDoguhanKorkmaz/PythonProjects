import sqlite3
import time

class Oyun():
    def __init__(self,isim,tur,yapimci,fiyat):
        self.isim = isim
        self.tur = tur
        self.yapimci = yapimci
        self.fiyat = fiyat
    def __str__(self):
        return ("Oyunun ismi = {}\nOyunun türü = {}\nOyunun yapımcısı = {}\nOyunun fiyatı = {} TL\n".format(self.isim,self.tur,self.yapimci,self.fiyat))

class Steam():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Steam.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists oyunlar (isim TEXT,tur TEXT,yapimci TEXT,fiyat INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def oyunlari_göster(self):
        sorgu = "Select * from oyunlar"
        self.cursor.execute(sorgu)
        oyunlar = self.cursor.fetchall()

        if (len(oyunlar) == 0):
            print("Hiç oyun bulunmamakta...")
        else:
            for i in oyunlar:
                oyun = Oyun(i[0],i[1],i[2],i[3])
                print(oyun)
    def oyun_ekle(self,oyun):
        sorgu = "INSERT INTO oyunlar Values(?,?,?,?)"
        self.cursor.execute(sorgu,(oyun.isim,oyun.tur,oyun.yapimci,oyun.fiyat))
        self.baglanti.commit()
    def oyun_sil(self,isim):
        sorgu = "Delete From oyunlar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    def isim_degistir(self,isim,yeni_isim):
        sorgu = "Select * From oyunlar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        oyunlar = self.cursor.fetchall()

        if (len(oyunlar) == 0):
            print("Hiç oyun bulunmamakta...")
        else:
            isim = oyunlar[0][0]
        #Veri Update etmek için kullanılan komut
        self.cursor.execute("Update oyunlar set isim = ? where isim =  ?",(yeni_isim,isim))
        self.baglanti.commit()
    def fiyat_degistir(self,isim,yeni_fiyat):
        sorgu = "Select * from oyunlar where isim=?"
        self.cursor.execute(sorgu,(isim,))

        oyunlar = self.cursor.fetchall()
        if (len(oyunlar) == 0):
            print("Hiç oyun bulunmamakta...")
        else:
            fiyat = oyunlar[0][3]

            self.cursor.execute("Update oyunlar set fiyat=? where isim=?",(yeni_fiyat,isim))
