import random

Soru = input("Lütfen sorunuzu buraya yazınız (örnek soru : bu benim için önemli mi ?) : ")

x = random.randrange(0,11)

if x < 5:
    print(Soru, "-------> EVET")
else:
    print(Soru, "------> HAYIR")
