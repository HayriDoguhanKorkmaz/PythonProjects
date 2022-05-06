import time
def tof(c):
    return c*1.8+32
def toc(f):
    return (f-32)/1.8
while True:
    print("""
    1. Fahreinet karşlığını bulmak istediğiniz Celcius derecesini bulmak için
    2. Celcius karşlığını bulmak istediğiniz Fahreinet derecesini bulmak için
    3. Çıkış için Q/q tuşuna basınız
    """)
    işlem = input("devam etmek için bir işlem seçmelisiniz : ")
    if (işlem == "1"):
        cDegeri = int(input("Fahreinet karşılığını bulmak istediğiniz Celcius değerini giriniz : "))
        print("{} C -> {} F".format(cDegeri,tof(cDegeri)))
    elif (işlem == "2"):
        fDegeri = int(input("Celcius karşılığını bulmak istedğiniz Fahreinet değerini giriniz : "))
        print("{} F -> {} C".format(fDegeri,toc(fDegeri)))
    elif (işlem == "Q") or (işlem == "q"):
        print("Uygulamadan çıkış yapılıyor...")
        time.sleep(1)
        print("uygulamadan çıkıldı...")
        break
    else:
        print("Geçersiz işlem doğru işlem giriniz...")
