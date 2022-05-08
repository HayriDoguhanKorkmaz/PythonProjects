import sqlite3
import time
import functools

class Sarki():
    def __init__(self,isim,sanatci,album,produksyon_sirketi,sarki_suresi):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.produksyon_sirketi = produksyon_sirketi
        self.sarki_suresi = sarki_suresi
    def __str__(self):
        return "Şarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksyon Şirketi: {}\nŞarkı Süresi: {}".format(self.isim,self.sanatci,self.album,self.produksyon_sirketi,self.sarki_suresi)


class Playlist():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("playlist.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists playlist (isim TEXT, sanatçı TEXT, albüm TEXT,prodüksyon şirketi TEXT, sarki_suresi INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def sarkilari_göster(self):
        sorgu = "Select * From playlist"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()
        if (len(sarkilar) == 0):
            print("Playlist'te hiç şarkı bulunmamakta...")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_ekle(self,sarki):
        sorgu = "Insert into playlist Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.produksyon_sirketi,sarki.sarki_suresi))
        self.baglanti.commit()
    def sarki_sil(self,isim):
        sorgu = "Delete From playlist where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    def toplam_playlist_suresi(self):
        toplam = 0
        sorgu = "Select * from playlist"
        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Playlistte hiç şarkı yok.")
        else:
            time = sarkilar[0][4]
            for i in range(time):
                toplam += i
        print(toplam)
                