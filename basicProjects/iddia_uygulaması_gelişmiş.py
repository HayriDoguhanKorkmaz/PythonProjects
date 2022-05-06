import random

for i in range(5):
    takimev = input("Ev sahibi takımın adını giriniz : ")
    takimdep = input("Deplasman takımın adını giriniz : ")
    rastgeleSayi = random.randrange(0,101)
    if rastgeleSayi < 10:
         print(takimev, "vs", takimdep, "maçını kazanacak takım", takimev)
    elif rastgeleSayi < 20:
        print(takimev, "vs", takimdep, "maçını kazananı dostluk")
    elif rastgeleSayi < 30:
        print(takimev, "vs", takimdep, "maçını kazanan takım", takimdep)
    elif rastgeleSayi < 40:
        print(takimev, "vs", takimdep, "karşılıklı gol var")
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


