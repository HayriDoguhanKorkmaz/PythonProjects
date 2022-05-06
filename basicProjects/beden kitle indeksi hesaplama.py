# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:12:13 2020

@author: DELL
"""

boy = float(input("boyunuzu metre cinsinden giriniz : "))
kilo = int(input("kilonuzu giriniz : "))

vki1 = boy*boy
vki = kilo / vki1
print(vki)

if vki < 18.5:
    print("Zayıfsınız")
elif vki < 25:
    print("Normal kilodasınız")
elif vki< 30:
    print("Fazla Kilolusunuz")
else:
    print("obezsiniz")
