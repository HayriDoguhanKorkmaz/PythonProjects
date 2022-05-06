import pyrebase

fireBase = pyrebase.initialize_app("https://algoritmadeneme-default-rtdb.europe-west1.firebasedatabase.app/")
db = fireBase.database()

def UrunEkle():
    tur = input("Eklemek istediğiniz ürünün türü : ")

    ad = input("Eklemek istediğiniz ürünün adı : ")
    veri = {"Tür" : tur,"Ad" : ad}
    db.child("tblMarket").push(veri)
def UrunleriGetir():
    urunler = db.child("tblMarket").get()

    for i in urunler:
        urun = i.val()
        print("Tür : {}, Ad : {}".format(urun["Tür"],urun["Ad"]))

def UrunSil(ad):
    urunler = db.child("tblMarket").get()
    for i in urunler:
        if i.val()["Ad"] == ad:
            db.child("tblMarket").child(i.key()).remove()
            print("Ürün silindi")
def UrunGuncelle():
    UrunleriGetir()
    tur = input("Güncellemek istediğiniz ürünün türünü giriniz : ")
    urunler = db.child("tblMarket").get()
    key = None
    for i in urunler:
        if i.val()["Tür"] == tur:
            key = i.key()
            pListesi = ["Tür","Ad"]
            parametre = int(input("Ürünün Türünü değiştirmek için = 1,Adını değiştirmek için = 2"))
            print("Yeni {} değerini giriniz : ".format(pListesi[parametre]))
            yeniDeger = input()
            db.child("tblMarket").child(key).update({pListesi[parametre]:yeniDeger})
            print("Güncelleme işlemi başarılı")
