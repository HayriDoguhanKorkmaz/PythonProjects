def durum(sicaklik,secim):
    nSu = [0,100]
    nDemir = [1538,2861]
    nCiva = [-38,356]
    n = [nSu,nDemir,nCiva]
    if sicaklik < n[secim][0]:
        print("Katı")
    elif sicaklik > n[secim][1]:
        print("Gaz")
    else:
        print("Sıvı")

secim = int(input("Su için 0, Demir için 1,Civa için 2 yi seçiniz : "))
sicaklik = int(input("Elementin sıcaklığını giriniz : "))
durum(sicaklik,secim)
