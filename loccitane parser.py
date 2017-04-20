# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:50:09 2016

@author: fialdm01
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import os
import pandas as pd
import re

start = time.clock()

chain_url = "http://www.loccitane.ru/boutique-locator,9,2,4321,6622.htm?Country=Russia"
addresses={'TK':[],'Address':[],'City':[]}

driver = webdriver.Chrome(r'C:\Users\FialDm01\Documents\Python Scripts\Parsers\chromedriver.exe')
driver.get(chain_url)
assert "Бутики" in driver.title
#search = driver.find_element_by_name('search')
#search.send_keys(query)
#search.send_keys(Keys.RETURN)
#sleep(3)
#assert "Бутики в Россия" in driver.title
html = driver.page_source
driver.close()

soup = BeautifulSoup(html, 'html.parser')
#driver.close()
for i in soup.findAll('div',{'class':'store-info-container'}):
    try:
        x=BeautifulSoup(str(i), 'html.parser').findAll('li')
        addresses['TK'].append(x[0].text)
        if re.findall("<li>(.*)<br/>", str(x[1]))!=[]:
            addresses['Address'].append(re.findall("<li>(.*)<br/>", str(x[1]))[0])
        else:
            addresses['Address'].append("")
        if re.findall("<br/>(.*)</li>", str(x[1]))!=[]:
            addresses['City'].append(re.findall("<br/>(.*)</li>", str(x[1]))[0])
        else:
            addresses['City'].append("")
    except:
        pass

#for i in soup.findAll('div',{'class':'store-info-container'}):
#    addresses['Address'].append(i.text)
#
#
#i=soup.findAll('div',{'class':'store-info-container'})[100]

addr=pd.DataFrame(addresses)
addr.drop_duplicates(subset='Address',inplace=True)

addr.to_csv(os.curdir+"L'occitane addresses.csv", sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))