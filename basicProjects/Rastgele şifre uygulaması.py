import random
import time

sayı1 = random.randrange(0,10)
sayı2 = random.randrange(0,10)
sayı3 = random.randrange(0,10)
sayı4 = random.randrange(0,10)
sayı5 = random.randrange(0,10)
sayı6 = random.randrange(0,10)
sayı7 = random.randrange(0,10)
sayı8 = random.randrange(0,10)
sayı9 = random.randrange(0,10)

şifreler = []

print("şifreniz oluşturuluyor")
time.sleep(1)
print("Şifreniz = {}{}{}{}{}{}{}{}{}".format(sayı1,sayı2,sayı3,sayı4,sayı5,sayı6,sayı7,sayı8,sayı9))

şifre = sayı1,sayı2,sayı3,sayı3,sayı5,sayı6,sayı7,sayı8,sayı9

şifreler.append(şifre)

print(şifreler)
