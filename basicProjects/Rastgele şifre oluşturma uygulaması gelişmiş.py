import random

kucuk = "abcdefghijklmnopqrstuvwxyz"
buyuk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayi = "0123456789"
sembol = "[]{}()*;/,._-"

hepsi = kucuk + buyuk + sayi + sembol
uzunluk = int(input("şifrenizin uzunluğu kaç karakter olsun : "))
lenght = uzunluk
sifre = "".join(random.sample(hepsi, lenght))
print(sifre)