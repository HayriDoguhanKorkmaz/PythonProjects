import random

ogrenciListesi = []
for i in range(20):
    ort = random.randrange(0,101)
    durum = "Hesaplanmadı"
    ogrenciListesi.append([ort,durum])

enBuyuk = 0
enKucuk = 100
toplam = 0
for i in ogrenciListesi:
    toplam += i[0]
    if i[0] > enBuyuk:
        enBuyuk = i[0]
    if i[0] < enKucuk:
        enKucuk = i[0]
ort = toplam/20


toplam = 0
cSayısı = 0
for i in ogrenciListesi:
    if i[0]==enKucuk or i[0]==enBuyuk:
        cSayısı += 1
        continue
    toplam += i[0]
yeniOrtalama = toplam/(20 - cSayısı)
print("Çan eğrisi ortalama değeri = {}".format(yeniOrtalama))

for i in ogrenciListesi:
    if i[0]<yeniOrtalama:
        i[1] = "Kaldı"
    else:
        i[1] = "Geçti"

toplamKaldı = 0
toplamGeçti = 0
for i in ogrenciListesi:
    if i[1] == "Kaldı":
        toplamKaldı += 1
    else:
        toplamGeçti += 1

print(ogrenciListesi)
print("Geçen Öğrenci sayısı = {}".format(toplamGeçti))
print("Kalan öğrenci sayısı = {}".format(toplamKaldı))
