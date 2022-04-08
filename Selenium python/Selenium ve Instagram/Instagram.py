from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:/Users/DELL/Desktop/chromedriver.exe')
browser.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(2)


girisYap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[2]/p/a")
girisYap.click()
time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("hesabın adını yaz")
password.send_keys("hesabın şifresini yaz")


loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")
loginButton.click()
time.sleep(5)


#Çıkan bildirimler içinde tıklama kodu başlangıcı.
notTodayButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
notTodayButton.click()
time.sleep(1)

notTodayButton2 = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
notTodayButton2.click()
time.sleep(1)
#Çıkan bildirimler içinde tıklama kodu bitişi.

#profile gitmek için direkt link kullanıldı.
profileButton = browser.get("https://www.instagram.com/hayridkorkmaz/")

time.sleep(1)


buttons = browser.find_elements_by_css_selector(".Y8-fY")
followersButton = buttons[1]
followersButton.click()
time.sleep(5)


#Scroll özelliği için javascript komutları başlangıcı.
jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
#Scroll özelliği için javascript komutları bitişi.


followersList = []
followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
for follower in followers:
    followersList.append(follower.text)

with open("Followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

browser.close()
