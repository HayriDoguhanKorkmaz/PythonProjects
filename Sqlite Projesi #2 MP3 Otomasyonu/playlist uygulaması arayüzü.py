from playlist import *
import time

print("""
***********************************************
Müzik Çalar Uygulamasına Hoş Geldiniz

İşlemler;
1.Müzikleri Göster
2.Müzik Ekle
3.Müzik Sil
4.Playlist Süresi

Çıkış için 'q' tuşuna basınız
***********************************************
""")

playlist = Playlist()

while True:
    seçim= input("Yapmak istediğiniz işlemi seçiniz : ")
    if (seçim == "q"):
        print("Uygulamadan çıkış yapılıyor...")
        time.sleep(2)
        print("Uygulamadan çıkış yapıldı...")
        break
    elif (seçim == "1"):
        playlist.sarkilari_göster()
    elif (seçim == "2"):
        isim = input("İsim:")
        sanatçı = input("Sanatçı:")
        albüm = input("Albüm:")
        prodüksyon_şirketi = input("Prodüksyon Şirketi:")
        süre = float(input("Şarkı Süresi:"))
        print("şarkı ekleniyor....")
        yeni_şarkı = Sarki(isim, sanatçı, albüm, prodüksyon_şirketi, süre)
        time.sleep(2)
        playlist.sarki_ekle(yeni_şarkı)
        print("Şarkı eklendi...")
    elif (seçim == "3"):
        isim = input("silmek istediğiniz şarkının ismi: ")
        cevap = input("Şarkıyı silmek istediğinize emin misiniz? (e/h)")
        if (cevap == "e"):
            playlist.sarki_sil(isim)
            print("Şarkı siliniyor...")
            time.sleep(2)
            print("Şarkı silindi")
    elif (seçim == "4"):
        playlist.toplam_playlist_suresi()
    else:
        print("Geçersiz işlem yapıldı lütfen doğru tuşlama yapınız...")
