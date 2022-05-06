# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:12:05 2020

@author: DELL
"""
import time 
print("-------------HESAP MAKİNESİ---------------")

print('''
             1. toplama işlemi
             2. çarpma işlemi
             3. çıkartma işlemi
             4. bölme işlemi''')
         

print("-------------------------------------------")
işlem = input("Yapmak istediğiniz işlemi seçiniz : ")
print("bu biraz sürebilir")
time.sleep(1)
if işlem == "1":
    print("toplama işlemi yapmaktasınız")
    Top1 = int(input("İlk sayı : "))
    Top2 = int(input("ikinci sayı : "))
    Topsonuc = Top1 + Top2
    print("cevabınız hesaplanıyor lütfen bekleyiniz.")
    time.sleep(0.5)
    print("{} ile {} in toplamı {} dir".format(Top1,Top2,Topsonuc))
        
elif işlem == "2":
    print("çarpma işlemi yapmaktasınız")
    çarp1 = int(input("İlk sayı : "))
    çarp2 = int(input("ikinci sayı : "))
    çarpsonuc= çarp1 * çarp2
    print("cevabınız hesaplanıyor lütfen bekleyiniz.")
    time.sleep(0.5)
    print("{} ile {} in çarpımı {} dir".format(çarp1,çarp2,çarpsonuc))
        
elif işlem == "3":
    print("çıkartma işlemi yapmaktasınız")
    çık1 = int(input("İlk sayı : "))
    çık2 = int(input("ikinci sayı : "))
    çıksonuc = çık1 - çık2
    print("cevabınız hesaplanıyor lütfen bekleyiniz.")
    time.sleep(0.5)
    print("{} ile {} in çıkartması {} dir".format(çık1,çık2,çıksonuc))
        
elif işlem == "4":
    print("bölme işlemi yapmaktasınız")
    böl1= int(input("İlk sayı : "))
    böl2= int(input("ikinci sayı : "))
    bölsonuc = böl1 / böl2
    print("cevabınız hesaplanıyor lütfen bekleyiniz.")
    time.sleep(0.5)
    print("{} ile {} in bölümü {} dir".format(böl1,böl2,bölsonuc))
else:
    print("hatalı işlem girdiniz")
    
        
        
