import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
#https://myaccount.google.com/lesssecureapps burdan hesabını açmalısın yoksa göndermez

yazan = input("Lütfen e-posta adresinizi giriniz : ")
sifre = input("Lütfen e-posta şifrenizi giriniz : ")
alan = input("E-postayı göndermek istediğiniz kişinin e-mail adresini giriniz : ")
icerik = input("İletmek istediğiniz mesajı giriniz : ")

mesaj = MIMEMultipart()

mesaj["From"] = yazan

mesaj["To"] = alan

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = icerik

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(yazan,sifre)
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail başarıyla gönderildi...")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu.....")
    sys.stderr.flush()
