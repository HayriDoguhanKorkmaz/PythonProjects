from selenium import webdriver
import random
import time

browser = webdriver.Chrome(executable_path='C:/Users/DELL/Desktop/chromedriver.exe')

url = "https://eksisozluk.com/besiktas--37894"

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,2)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entries.append(element.text) 

    time.sleep(3)
    pageCount += 1
with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+".\n"+entry+"\n")
        file.write("*************************************")
        entryCount += 1

browser.close()

