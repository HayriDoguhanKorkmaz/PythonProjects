sayi = int(input("Bitiş Sayısını Giriniz : "))
toplamT = 0
toplamC = 0
for i in range(0,sayi):
    if(i % 2 == 0):
        toplamC += i
    else:
        toplamT += i

print(toplamT)
print(toplamC)
