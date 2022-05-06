import random

İsim = input("Lütfen adınızı giriniz : ")

x = random.randrange(0,101)

if x < 10:
    print(İsim, "Bugün mavi renk oje sürmelisin")
elif x < 20:
    print(İsim, "Bugün kırmızı renk oje sürmelisin")
elif x < 30:
    print(İsim, "Bugün turuncu renk oje sürmelisin")
elif x < 40:
    print(İsim, "Bugün siyah renk oje sürmelisin")
elif x < 50:
    print(İsim, "Bugün beyaz renk oje sürmelisin")
elif x < 60:
    print(İsim, "Bugün altın rengi oje sürmelisin")
elif x < 70:
    print(İsim, "Bugün mor renk oje sürmelisin")
elif x < 80:
    print(İsim, "Bugün şeffaf renk oje sürmelisin")
elif x < 90:
    print(İsim, "Bugün pembe renk oje sürmelisin")
else:
    print(İsim, "Bugün oje sürmemelisin")
