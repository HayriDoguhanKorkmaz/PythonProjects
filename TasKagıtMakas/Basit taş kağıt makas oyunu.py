import random
print("""
      Taş Kağıt Makas Oyununa Hoşgeldiniz
      1.Taş
      2.Kağıt
      3.Makas
      ÇIKIŞ İÇİN 4
      """)
while True:
    Hamle = int(input("Hamlenizi giriniz : "))
    karşı_hamle = random.randint(-1,4)
    if (Hamle == 1):
        print("Taşı seçtiniz")
        if (Hamle == karşı_hamle):
            print("Oyun berabere")
        elif (Hamle > karşı_hamle):
            print("Oyunu kazandınız")
        else:
            print("Oyunu kaybettiniz")
    elif (Hamle == 2):
        print("Kağıdı seçtiniz")
        if (Hamle == karşı_hamle):
            print("Oyun berabere")
        elif (Hamle > karşı_hamle):
            print("Oyunu kazandınız")
        else:
            print("Oyunu kaybettiniz")
    elif (Hamle == 3):
        print("Makası seçtiniz")
        if (Hamle == karşı_hamle):
            print("Oyun berabere")
        elif (Hamle > karşı_hamle):
            print("Oyunu kazandınız")
        else:
            print("Oyunu kaybettiniz")        
    elif (Hamle == 4):
        print("Çıkış yapılıyor...")
        break
    else:
        print("hatalı işlem seçtiniz")
        break

