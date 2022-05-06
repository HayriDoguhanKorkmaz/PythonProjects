import random
import time

print("""
****************************************
Kelime Tahmin Oyununa Hoşgeldiniz
****************************************
""")

secim = input("Devam etmek için E/e çıkış yapmak için Q/q : ")
while True:
    if (secim == "Q") or (secim == "q"):
        print("oyundan çıkılıyor...")
        time.sleep(0.5)
        print("Oyun sona erdi...")
        break
    elif (secim == "E") or (secim == "e"):
        RastgeleSayı = random.randrange(1,100)
        HakSayısı = 4
        while True:
            tahmin = int(input("Tahmininizi giriniz (çıkış için 0) : "))
            if (tahmin == RastgeleSayı):
                print("Tebrikler tahmininiz doğru cevap = {}".format(RastgeleSayı))
                break
            elif (tahmin < RastgeleSayı):
                HakSayısı -= 1
                print("{} Hakkınız kaldı ".format(HakSayısı))
                print("Cevap tahmininizden daha büyük")
                if (HakSayısı == 0):
                    print("Tahmin haklarınız bitti cevap = {}".format(RastgeleSayı))
                    break
            elif (tahmin > RastgeleSayı):
                HakSayısı -= 1
                print("{} Hakkınız kaldı ".format(HakSayısı))
                print("Tahmininiz cevaptan daha küçük")
                if (HakSayısı == 0):
                    print("Tahmin haklarınız bitti cevap = {}".format(RastgeleSayı))
                    break
    else:
        print("lütfen doğru kodlama yapınız...")