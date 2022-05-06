import random
while True:
    isimkendin = input("Kendi isminizi giriniz : ")
    isimkiz = input("Kız arkadaşınızın ismini giriniz : ")
    
    rastgeleSayi = random.randrange(0,101)
    if rastgeleSayi < 33:
         print(isimkendin, isimkiz, "yüzde", rastgeleSayi, "bu ilişki bozuk")
   
    elif rastgeleSayi < 66:
         print(isimkendin, isimkiz, "yüzde", rastgeleSayi, "oluru var")
    else:
         print(isimkendin, isimkiz, "yüzde", rastgeleSayi, "birbiriniz için yaratılmışsınız")

    işlem = input("Çıkmak için Q devam etmek için A tuşuna basınız.")

    if işlem == "Q" or işlem == "q":
        quit()
    
    else:
        pass

      
                  



