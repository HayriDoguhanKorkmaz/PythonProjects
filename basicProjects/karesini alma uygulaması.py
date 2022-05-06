sayi = int(input("Lütfen buraya bir sayı giriniz : "))

def karesiniAl():
    if sayi == 0:
        print("Lütfen sıfırdan farklı bir sayı giriniz")
        return
    elif sayi > 0:
        carpim = sayi * sayi
        print(sayi, "nin karesi --->", carpim)

karesiniAl()

