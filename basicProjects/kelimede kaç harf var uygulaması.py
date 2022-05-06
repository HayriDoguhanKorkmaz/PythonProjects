kelime = input("kaç harf olduğunu öğrenmek istediğiniz cümleyi giriniz : ").replace(" ", "")

ortak = list(kelime)

for i in ortak:
    print("{} harfinde => {} tane var".format(i, kelime.count(i)))