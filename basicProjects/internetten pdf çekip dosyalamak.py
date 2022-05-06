import requests
import re

d = open("data.txt","a")

url = "http://slav0nic.org.ua/static/books/python/"

website = requests.get(url)

html = website.text 

dosya = re.findall('href="(.*pdf)"',html)

for dosyaici in sorted(x for x in (dosya)):
    d.write(url + dosyaici+"\n")
d.close()
    
    
