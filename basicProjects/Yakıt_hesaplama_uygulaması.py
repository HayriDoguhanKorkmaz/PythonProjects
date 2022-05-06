# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:47:44 2020

@author: DELL
"""
#aşağıdaki istenen veri aracın km de yaktığı yakıttır.

kmBenzin = float(input("aracın kilometrede yaktığı benzin miktarını giriniz : "))

#aşağıdaki veri aracın ne kadar yol aldığını istemektedir

yol = int(input("aracın aldığı yolu kilometre cinsinden yazınız : "))

#formül gayet basit (yol X kmBenzin = depoyu fulleyen para )

fulldepo = (kmBenzin * yol)

print("Arabanız bu kadar paraya deposunu doldurmaktadır", fulldepo)
