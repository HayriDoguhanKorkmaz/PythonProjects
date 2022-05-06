print("""
********************************************************      
      ATM UYGULAMASINA HOŞGELDİNİZ...
1.Bakiye Sorgulama      
2.Para Yatırma      
3.Para Çekme

      ÇIKIŞ İÇİN 'q' TUŞUNA BASINIZ.
********************************************************
             """)

Bakiye = 1000

while True:
    işlem = input("Seçtiğiniz işlemi buraya giriniz : ")
    
    if (işlem == "q"):
        print("Hoşcakalın")
        break
    elif (işlem == "1"):
        print("bakiyeniz {} türk lirasıdır".format(Bakiye))
    elif (işlem == "2"):
        paraEkle = int(input("girmek istediğiniz miktarı seçiniz : "))
        
        Bakiye += paraEkle
    
    elif (işlem == "3"):
        paraÇek = int(input("çekmek istediğiniz miktarı giriniz : "))
        
        if (Bakiye - paraÇek < 0):
            print("İstediğiniz miktar kadar paraya sahip değilsiniz")
            continue
        Bakiye -= paraÇek
    else:
        print("Geçersiz işlem...")
