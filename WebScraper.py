from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)


        
for i in range(6):
    dny=[]
    
    if i == 0:
        driver.get('https://myanimelist.net/profile/RDGames1000')
    if i == 1:
        driver.get('https://myanimelist.net/profile/zbynek0303')
    if i == 2:
        driver.get('https://myanimelist.net/profile/Lukas1234567')
    if i == 3:
        driver.get('https://myanimelist.net/profile/chazp246')
    if i == 4:
        driver.get('https://myanimelist.net/profile/Betlik3')
    if i == 5:
        driver.get('https://myanimelist.net/profile/IllicNightspear')

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    dny = soup.find_all('div', {'class':"di-tc al pl8 fs12 fw-b"})
    pocet=dny[0]
    pocet = str(pocet)
    print(pocet)
    print(pocet[77:-6])
    pocet = pocet[77:-6]

    if i == 0:
        roman = [pocet]
    if i == 1:
        zbynek = [pocet]
    if i == 2:
        lukas = [pocet]
    if i == 3:
        zahy = [pocet]
    if i == 4:
        prokop = [pocet]
    if i == 5:
        aram = [pocet]



data = {'Roman':roman,'Zbynek':zbynek,'Lukas':lukas,'Zahalka':zahy,'Prokop':prokop,'Aram':aram}
columns = ('Roman', 'Zbynek', 'Lukas', 'Zahalka', 'Prokop', 'Aram')
df = pd.DataFrame(data=data, columns=columns)
df.to_excel('pocetdnu.xlsx')
