import time
class Bilgisayar():
    def __init__(self,pc_durum = "kapalı",pc_ses = 30,uygulama_listesi = ["Google Explorer"], açık_olan_uygulama = "yok"):  
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.uygulama_listesi = uygulama_listesi
        self.açık_olan_uygulama = açık_olan_uygulama
    
    def Pc_Aç(self):
        if (self.pc_durum == "açık"):
            print("Bilgisayar zaten açık.")
        else:
            şifre = input("Bilgisayar parolasını giriniz : ")
            if (şifre == "Hayri123"):
                print("Bilgisayar açılıyor..")
                time.sleep(1)
                print("Bilgisayar açıldı Hoşgeldiniz..")
                self.pc_durum = "açık"
            else:
                print("hatalı şifre girdiniz Bilgisayar kapanıyor..")
                self.pc_durum = "kapalı"
    def Pc_Kapat(self):
        if (self.pc_durum == "kapalı"):
            print("Bilgisayar zaten kapalı.")
        else:
            print("Bilgisayar Kapanıyor Hoşçakalın...")
            time.sleep(1)
            print("Bilgisayar kapandı.")
            self.pc_durum = "kapalı"
    def yeniden_başlat(self):
        while True:
            işlem = input("Bilgisayarı yeniden başlatmak ister misiniz ? 'evet/hayır' : ")
            if (işlem == "evet" and self.pc_durum == "açık"):
                print("Bilgisayar yeniden başlatılıyor...")
                time.sleep(1)
                print("Bilgisayar açılıyor...")
                time.sleep(1)
                şifre = input("Bilgisayar parolasını giriniz : ")
                if (şifre == "Hayri123"):
                    print("Bilgisayar açılıyor..")
                    time.sleep(1)
                    print("Bilgisayar açıldı Hoşgeldiniz..")
                    self.pc_durum = "açık"
                    break
            elif (işlem == "evet" and self.pc_durum == "kapalı"):
                print("bilgisayar kapalı iken yeniden başlatılamaz")
                break
            else:
                break
    def Ses_Ayarları(self):
        while True:
            if (self.pc_durum == "kapalı"):
                print("Bilgisayar kapalı iken ses ayarı yapamazsınız..")
                break
            işlem = input("Sesi açmak için = +\nSesi azaltmak için = -\n Çıkış için 'q'\n : ")
            if (işlem == "+"):
                if (self.pc_ses != 100):
                    self.pc_ses += 1
                    print("ses =",self.pc_ses)
            elif (işlem == "-"):
                if(self.pc_ses != 0):
                    self.pc_ses  -= 1
                    print("ses = ",self.pc_ses)
            else:
                print("Ses güncellendi = ",self.pc_ses)
                break
    def Uygulama_yükle(self,uygulama_ismi):
        if (self.pc_durum == "kapalı"):
                print("Bilgisayar kapalı iken uygulama yükleyemezsiniz..")
        elif (self.pc_durum == "açık"):
            print("uygulama ekleniyor...")
            time.sleep(1)
            self.uygulama_listesi.append(uygulama_ismi)
            print("uygulama eklendi")
    def Uygulama_Aç(self,uygulama_ismi):
        if (self.pc_durum == "kapalı"):
                print("Bilgisayar kapalı iken uygulama açamazsınız..")
        if (uygulama_ismi in uygulama_listesi):
            print("uygulama açılıyor")
            time.sleep(0.5)
            print("uygulama açıldı..")
            self.açık_olan_uygulama = uygulama_ismi
        else:
            print("Açmak istediğiniz uygulama yüklü değil")
    def Bilgisayarı_Sıfırla(self):
        if (self.pc_durum == "kapalı"):
                print("Bilgisayar kapalı iken bilgisayarı sıfırlayamazsınız..")
        elif (self.pc_durum == "açık"):
            işlem = input("Bilgisayarı sıfırlamak istediğinizden emin misiniz ? 'evet/hayır' ")
            while True:
                if (işlem == "evet"):
                    print("Bilgisayar sıfırlanıyor bu işlem biraz sürebilir")
                    time.sleep(3)
                    print("Bilgisayar yeniden başlatılıyor..")
                    time.sleep(1)
                    print("bilgisayar açılıyor..")
                    time.sleep(1)
                    print("Bilgisayar açıldı Hoşgeldiniz..")      
                    self.uygulama_listesi.clear()
                    self.açık_olan_uygulama = "yok"
                    break
                else:
                    break
    def __len__(self):
        return len(self.uygulama_listesi)
    def __str__(self):
        return "Pc durumu = {}\n Ses durumu = {}\n Yüklü uygulamalar = {}\n Açık olan uygulama = {}\n".format(self.pc_durum, self.pc_ses,self.uygulama_listesi,self.açık_olan_uygulama)
def Bilgisayar_Özellikleri():
    print("""
          işlemci = İntel Core i5
          Ekran Kartı = İnvidia Geforce 820M
          Ram = 8 GB (kullanılabilir 7.98)
          Yerel Disk = [//////////                  ]
                       1024 gb (kullanılabilir 780 gb)
          """)
bilgisayar = Bilgisayar()
print("""
      
     ** Bilgisayar uygulaması** 
        1.Bilgisayarı Aç
        2.Bilgisayarı Kapat
        3.Bilgisayarı Yeniden Başlat
        4.Ses Ayarları
        5.Uygulama Yükle
        6.Uygulama Aç
        7.Bilgisayarı Sıfırla
        8.Bilgisayar Bilgileri
        ÇIKIŞ İÇİN 'q' """)
while True:
    işlem = input("işlem seçiniz : ")
    if (işlem == "q"):
        print("işlem sonlandırılıyor")
        break
    elif (işlem == "1"):
        bilgisayar.Pc_Aç()
    elif (işlem == "2"):
        bilgisayar.Pc_Kapat()
    elif (işlem == "3"):
        bilgisayar.yeniden_başlat()
    elif (işlem == "4"):
        bilgisayar.Ses_Ayarları()
    elif (işlem == "5"):
        uygulama_isimleri = input("uygulama isimlerini virgül ile ayırarak giriniz : ")  
        uygulama_listesi = uygulama_isimleri.split(",")  
        for eklenecekler in uygulama_listesi:
            bilgisayar.Uygulama_yükle(eklenecekler)
    elif (işlem == "6"):
        uygulama_ismi = input("açmak istediğiniz uygulamayı giriniz : ")
        bilgisayar.Uygulama_Aç(uygulama_ismi)
    elif (işlem == "7"):
        bilgisayar.Bilgisayarı_Sıfırla()
    elif (işlem == "8"):
        print(bilgisayar)
        print(Bilgisayar_Özellikleri())
    else:
        print("geçersiz işlem")