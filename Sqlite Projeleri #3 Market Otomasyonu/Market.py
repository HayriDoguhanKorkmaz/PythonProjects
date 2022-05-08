import sqlite3
import time

class Ürün():
    def __init__(self,isim,tür,gramaj,marka,fiyat):
        self.isim = isim
        self.tür = tür
        self.gramaj = gramaj
        self.marka = marka
        self.fiyat = fiyat
    def __str__(self):
        return "Ürünün ismi: {}\nÜrünün türü: {}\nÜrünün gramajı: {}\nÜrünün markası: {}\nÜrünün fiyatı: {} TL".format(self.isim,self.tür,self.gramaj,self.marka,self.fiyat)


class Market():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists market (isim TEXT, tür TEXT,gramaj INT,marka TEXT,fiyat INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def urunleri_goster(self):
        sorgu = "Select * From market"

        self.cursor.execute(sorgu)

        urunler = self.cursor.fetchall()

        if (len(urunler) == 0):
            print("Markette hiçbir ürün bulunmamaktadır...")
        else:
            for i in urunler:
                urun = Ürün(i[0],i[1],i[2],i[3],i[4])
                print(urun)
    def ürün_ekle(self,ürün):
        sorgu = "Insert into market Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(ürün.isim,ürün.tür,ürün.gramaj,ürün.marka,ürün.fiyat))
        self.baglanti.commit()
    def ürün_sil(self,isim):
        sorgu = "Delete From market where isim = ?"
        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def fiyat_degistir(self,isim,yeni_fiyat):
        sorgu = "Select * From market where isim=?"
        self.cursor.execute(sorgu,(isim,))
        urunler = self.cursor.fetchall()
        if (len(urunler) == 0):
            print("Hiç ürün bulunmamakta...")
        else:
            fiyat = urunler[0][4]

            self.cursor.execute("Update market set fiyat=? where isim=?",(yeni_fiyat,isim))
            self.baglanti.commit()
    def isim_degistir(self,isim,yeni_isim):
        sorgu = "Select * from market where isim=?"
        self.cursor.execute(sorgu,(isim,))

        urunler = self.cursor.fetchall()
        if(len(urunler) == 0):
            print("Markette hiç ürün bulunmamaktadır...")
        else:
            isim = urunler[0][0]
            self.cursor.execute("Update market set isim=? where isim=?",(yeni_isim,isim))



        
