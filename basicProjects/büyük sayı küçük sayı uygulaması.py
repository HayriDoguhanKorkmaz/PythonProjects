# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:47:50 2021

@author: DELL
"""

vize1 = int(input("buraya bir sayı giriniz:"))
final = int(input("buraya bir sayı giriniz:"))

notlar = vize1*40/100 + final*60/100

if notlar > 90:
    print("AA ile geçtiniz notunuz {}".format(notlar))
elif notlar > 85:
    print("BA ile geçtiniz notunuz {}".format(notlar))
elif notlar > 80:
    print("BB ile geçtiniz notunuz {}".format(notlar))
elif notlar > 75:
    print("CB ile geçtiniz notunuz {}".format(notlar))
elif notlar > 70:
    print("CC ile geçtiniz notunuz {}".format(notlar))
elif notlar > 65:
    print("DC ile geçtiniz notunuz {}".format(notlar))  
elif notlar > 60:
    print("DD ile geçtiniz notunuz {}".format(notlar))
elif notlar > 55:
    print("FD ile geçtiniz notunuz {}".format(notlar))
elif notlar >= 50:
    print("FF ile geçtiniz notunuz {}".format(notlar))
else:
    print("kaldınız notunuz {}".format(notlar))