import requests
from bs4 import BeautifulSoup
import time
url = "https://www.doviz.com/"

response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
euro = soup.find("span",{"data-socket-key":"EUR"})
dolar = soup.find("span",{"data-socket-key":"USD"})
altın = soup.find("span",{"data-socket-key":"gram-altin"})

euro = euro.text
dolar = dolar.text
altın = altın.text
while True:
    print("""
    1.Kurları öğrenmek için
    cıkış için q/Q 
    """)
    islem = input("yapmak istediğiniz islemi seciniz:")
    if (islem=="q") or (islem == "Q"):
        break
    elif (islem =="1"):
        print("Euro:",euro)
        print("Dolar:",dolar)
        print("Altın:",altın)
