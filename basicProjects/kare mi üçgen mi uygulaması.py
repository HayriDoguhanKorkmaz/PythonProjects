# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:31:14 2021

@author: DELL
"""

print('''1. Dörtgen
         2. Üçgen''')

x = input("Buraya yapmak istediğniz işlemi seçiniz :")

if x == "1":
    print(''' 1.kare
              2. dikdörtgen
              3. dörtgen ''')
    y = input("Buraya yapmak istediğniz işlemi seçiniz :")
    k1 = int(input("ilk kenarı giriniz :"))
    k2 = int(input("ikinci kenarı giriniz :"))
    k3 = int(input("üçüncü kenarı giriniz :"))
    k4 = int(input("dördüncü kenarı giriniz :"))
    if y  == "1":
        if k1==k2 and k3==k4:
            print("girdiğiniz sayılara göre bu bir kare")
        else:
            print("hatalı sayılar girdiniz")
    elif y =="2":
        if k1!=k2 and k3==k4:
            print("girdiğiniz sayılara göre bu bir dikdörtgen")
        else:
            print("hatalı sayılar girdiniz")
    else:
        print("girdiğiniz sayılara göre bu bir dörtgen")
else:
    a = int(input("ilk kenarı giriniz :"))
    b = int(input("ikinci kenarı giriniz :"))
    c = int(input("üçüncü kenarı giriniz :"))
    if a==b and b!=c:
        print("Üçgen ikizkenardır")
    elif c==b and a!=b:
        print("Üçgen ikizkenardır")
    elif a==c and b!=c:
        print("Üçgen ikizkenardır")
    elif a==b and b==c:
        print("üçgen eşkenar üçgendir")
    else:
        print("üçgen sıradan bir üçgendir")
    