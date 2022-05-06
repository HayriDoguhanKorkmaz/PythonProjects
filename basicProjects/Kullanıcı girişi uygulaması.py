# -*- coding: utf-8 -*-
print("""
      *****************************
      Kullanıcı Girişi Programı
      *****************************
      """)

sys_kullanıcıadı = "HayriDK"
sys_parola = "12345"
giriş_hakkı = 3
while True:
    kullanıcıadı = input("Kullanıcı Adınızı giriniz : ")
    parola = input("Parolanızı Giriniz : ")
    if (kullanıcıadı != sys_kullanıcıadı and parola == sys_parola):
        print("kullanıcı adınız hatalı...")
        giriş_hakkı -= 1 
    elif (kullanıcıadı == sys_kullanıcıadı and parola != sys_parola):
        print("Parolanız hatalı...")
        giriş_hakkı -= 1 
    elif (kullanıcıadı != sys_kullanıcıadı and parola != sys_parola):
        print("Hem parolanız hemde kullanıcı adınız hatalı...")
        giriş_hakkı -= 1
    else:
        print("Sisteme giriş yapıldı...")
        break
    if giriş_hakkı == 0:
        print("giriş hakkınız bitti...")
        break
        
        