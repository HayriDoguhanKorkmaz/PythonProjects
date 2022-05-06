toplamHesapla = lambda k: sum(range(1, int(k)+1))
k = input("1'den kaça kadar sayıların toplamını istersiniz : ")
print("1'den {}'a kadar sayıların toplamı {}".format(k, toplamHesapla(k)))

