import random


while True:
    takimev = input("Ev sahibi takımın adını giriniz : ")
    takimdep = input("Deplasman takımın adını giriniz : ")
    rastgeleSayi = random.randrange(0,101)
    if rastgeleSayi < 10:
        print(takimev, "vs", takimdep, "maçı kazanacak takım", takimev)    
    elif rastgeleSayi < 20:
        print(takimev, "vs", takimdep, "maçın kazananı dostluk")
    elif rastgeleSayi < 30:
        print(takimev, "vs", takimdep, "maçı kazanan takım", takimdep)
    elif rastgeleSayi < 40:
        print(takimev, "vs", takimdep, "maçı 1,5 üst")        
    elif rastgeleSayi < 50:
        print(takimev, "vs", takimdep, "karşılıklı gol yok")
    elif rastgeleSayi < 60:
        print(takimev, " vs", takimdep, "2,5 üst")
    elif rastgeleSayi < 70:
        print(takimev, "vs", takimdep, "2,5 alt")
    elif rastgeleSayi < 80:
        print(takimev, "vs", takimdep, "1,5 üst")
    elif rastgeleSayi < 90:
        print(takimev, "vs", takimdep, "3,5 üst")
    else:
        print(takimev, "vs", takimdep, "+6 gol")

    işlem = input("Çıkmak için Q ya devam etmek için a'ya basınız : ")

    if işlem == "Q" or işlem == "q":
        quit()
    else:
        pass



