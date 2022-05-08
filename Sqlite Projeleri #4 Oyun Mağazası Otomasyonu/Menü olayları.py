from steam import *
import time

print("""
Steam uygulamasına hoşgeldiniz
işlemler;
1.Oyunları Göster
2.Oyun Ekle
3.Oyun Sil
4.Oyun Adını Değiştir
5.Fiyat değiştir
Çıkış için 'Q/q' tuşuna basınız
""")

steam = Steam()

while True:
    islem = input("Yapmak istediğiniz işlemi giriniz : ")
    if (islem == "q") or (islem == "Q"):
        print("Uygulamadan çıkış yapılıyor...")
        time.sleep(0.8)
        print("Uygulama sona erdi...")
        break
    elif (islem == "1"):
        steam.oyunlari_göster()
    elif (islem == "2"):
        isim = input("Eklemek istediğiniz oyunun adı : ")
        time.sleep(0.4)
        tur = input("Eklemek istediğiniz oyunun türü : ")
        time.sleep(0.4)
        yapimci = input("Eklemek istediğiniz oyunun yapımcısı : ")
        time.sleep(0.4)
        fiyat = int(input("Eklemek istedğiniz oyunun fiyatı : "))
        time.sleep(0.6)
        print("Oyun ekleniyor...")
        time.sleep(0.8)
        yeni_oyun = Oyun(isim,tur,yapimci,fiyat)
        steam.oyun_ekle(yeni_oyun)
        print("Oyun eklendi.")
    elif (islem == "3"):
        isim = input("Silmek istediğiniz oyunun ismi : ")
        cevap = input("Oyunu silmek istediğinize emin misiniz e/h : ")
        if cevap == "e":
            print("Oyun siliniyor...")
            time.sleep(0.8)
            steam.oyun_sil(isim)
            print("Oyun silindi")
        else:
            continue
    elif (islem == "4"):
        isim = input("İsmini değiştirmek istediğiniz oyunun adı : ")
        time.sleep(0.8)
        yeni_isim = input("Oyunun yeni adı : ")
        steam.isim_degistir(isim,yeni_isim)
        print("Oyunun adı değiştirildi")
    elif (islem=="5"):
        isim = input("Fiyatını güncellemek istediğiniz oyunun adını giriniz : ")
        yeni_fiyat = int(input("Yeni fiyat bilgisini giriniz : "))
        steam.fiyat_degistir(isim,yeni_fiyat)
        time.sleep(1)
        print("oyunun fiyatı başarı ile güncellendi")
    else:
        print("Lütfen doğru kodlama yapınız...")
