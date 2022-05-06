import time
import random

class Kumanda():
    def __init__(self,TV_durum = "kapalı", TV_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT",marka = "Beko",netflix = "kapalı"):
      self.TV_durum = TV_durum
      self.TV_ses = TV_ses
      self.kanal_listesi = kanal_listesi
      self.kanal = kanal
      self.marka = marka
      self.netflix = netflix
      
    def Tv_aç(self):
        if (self.TV_durum == "açık"):
            print("televizyon zaten açık")
        else:
            print("televizyon açılıyor")
            print("televizyon açıldı")
            self.TV_durum = "açık"
    def Tv_kapat(self):
        if (self.TV_durum == "kapalı"):
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapanıyor")
            print("televizyon kapandı")
            self.TV_durum = "kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("sesi azalt = '<'\n, sesi arttır = '>'\n,çıkış = çıkış")
            if (cevap == "<"):
                if (self.TV_ses != 0):
                    self.TV_ses -= 1
                    print("ses =", self.TV_ses)
            elif (cevap == ">"):
                if (self.TV_ses != 31):
                    self.TV_ses += 1
                    print("ses = ",self.TV_ses)
            else:
                print("tv sesi güncelendi = ",self.TV_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")
    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
    
        self.kanal = self.kanal_listesi[rastgele]
        
        print("su anki kanal : ", self.kanal)
        
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return " Marka = {} \n TV durumu = {}\n TV ses = {}\n Kanal Listesi = {}\n Şuanki kanal = {}\n Netflix = {}\n".format(self.marka,self.TV_durum,self.TV_ses,self.kanal_listesi,self.kanal,self.netflix)
    def netflix_aç(self):
        işlem = input("netflixi açmak istermisiniz evet/hayır çıkmak için 'q'")
        while True:
            
            if (işlem == "evet"):
                print("netflix açılıyor...")
                time.sleep(1)
                print("netflix açıldı")
                self.netflix = "açık"
                break
            elif (işlem == "hayır"):
                print("netflix kapanıyor...")
                time.sleep(1)
                self.netflix = "kapalı"
                break
            else:
                break
kumanda = Kumanda()

print("""
      
      Televizyon uygulaması
      
      1. TV Aç
      2. Tv Kapat
      3. Ses Ayarları
      4. Kanal Ekle
      5. Kanal Sayısını Öğrenme
      6. Rastgele Kanala Geçme
      7. Televizyon Bilgileri
      8. Netflixi Aç
      çıkmak için 'q' ya basınız
 """)
 
while True:
    işlem = input("işlem seçiniz : ")
    if (işlem == "q"):
        print("işlem sonlandırılıyor")
        break
    elif (işlem == "1"):
        kumanda.Tv_aç()
    elif (işlem == "2"):
        kumanda.Tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimleri = input("kanal isimlerini virgül ile ayırarak giriniz")
        
        kanal_listesi = kanal_isimleri.split(",")
        
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("kanal sayısı", len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    elif (işlem == "8"):
        kumanda.netflix_aç()
    else:
        print("geçersiz işlem")
