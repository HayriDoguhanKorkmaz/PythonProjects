isim = input("Lütfen isminizi giriniz : ")
for i in range(0, len(isim)):
    for j in range(0,i+1):
        print(isim[j],end= "")
    print("")
for i in range(len(isim)-1,0,-1):
    for j in range(0,i):
        print(isim[j],end = "")
    print("")
