from Market import *
import time


print("""
*******************************************************
Süper Market Uygulamasına Hoşgeldiniz

işlemler;
1.Ürünleri Göster
2.Ürün Ekle 
3.Ürün Sil
4.Ürünün Fiyatını Değiştir
5.Ürünün Adını Değiştir

Çıkış için 'q' tuşuna basınız.
*******************************************************
""")

market = Market()

while True:
    işlem = input("Yapmak istediğiniz işlemi tuşlayınız : ")
    if (işlem == "q"):
        print("Uygulamadan çıkış yapılıyor...")
        time.sleep(2)
        print("Uygulamadan kapandı...")
        break
    elif (işlem == "1"):
        market.urunleri_goster()
    elif (işlem == "2"):
        isim = input("Lütfen eklemek istediğiniz ürünün ismini giriniz : ")
        time.sleep(0.5)
        tür = input("Lütfen eklemek istedğiniz ürünün türünü giriniz : ")
        time.sleep(0.5)
        gramaj = int(input("Lütfen girmek istedğiniz ürünün miktarını/gramajını/adetini giriniz : "))
        time.sleep(0.5)
        marka = input("Lütfen girmek istediğiniz ürünün markasını giriniz  : ")
        time.sleep(0.5)
        fiyat = int(input("Lütfen girmek istediğiniz ürünün fiyatını giriniz : "))
        print("Ürün ekleniyor....")
        yeni_ürün = Ürün(isim,tür,gramaj,marka,fiyat)
        time.sleep(2)
        market.ürün_ekle(yeni_ürün)
        print("Ürün başarı ile eklendi....")
    elif (işlem == "3"):
        isim = input("Silmek istediğiniz ürünün ismi: ")
        cevap = input("Ürünü silmek istediğinize emin misiniz? (e/h)")
        if (cevap == "e"):
            print("Ürün siliniyor....")
            time.sleep(2)
            market.ürün_sil(isim)
            print("Ürün başarı ile silindi....")
        else:
            continue
    elif (işlem=="4"):
        isim = input("Fiyatını değiştirmek istediğiniz ürünün ismi : ")
        yeni_fiyat = int(input("Ürünün yeni fiyatını giriniz : "))
        market.fiyat_degistir(isim,yeni_fiyat)
        time.sleep(0.8)
        print("Fiyat değişikliği başarılı")
    elif (işlem == "5"):
        isim = input("İsmini değiştirmek istediniz ürünün adı : ")
        yeni_isim = input("Ürünün yeni adı : ")
        market.isim_degistir(isim,yeni_isim)
        time.sleep(0.8)
        print("Ürünün ismi başarı ile değiştirildi...")
    else:
        print("Geçersiz işlem girdiniz lütfen doğru tuşlama yapınız...")

