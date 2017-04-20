# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:52:42 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "http://kruger42.ru/index.php/shops"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')


cities=[str(i)[3:len(i)-5] for i in soup.find_all('b')]
cities+=[cities.pop(0)]

addresses={'City':[],'Street':[]}

r=1
for i in cities[:len(cities)-1]:
    for j in soup.find_all('td', valign="top")[r:r+1]: #Kemerovo - [len(soup.find_all('td', valign="top"))-3:]
        j=str(j)        
        street=re.findall(">([,\. А-Яа-я0-9]+)", j)
        addresses['City']+=[i for k in range(len(street))]
        addresses['Street']+=street
        if r<len(soup.find_all('td', valign="top"))-4:
            r+=1
        else:
            break
for j in soup.find_all('td', valign="top")[len(soup.find_all('td', valign="top"))-3:]:
    j=str(j)
    street=re.findall(">([,\. А-Яа-я0-9]+)", j)
    addresses['City']+=[cities[len(cities)-1] for k in range(len(street))]
    addresses['Street']+=street
    
addr=pd.DataFrame(addresses)
addr['Street']=addr['Street'].str.strip()
addr.drop_duplicates(subset='Street', inplace=True)

addr.to_csv(os.curdir+'Kruger42 addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))