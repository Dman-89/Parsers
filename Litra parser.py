# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:42:39 2016

@author: fialdm01
"""

import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "http://litra-beer.ru/magazini"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')
addresses = {'City & Street':[],'Region':[],'coords':[]}
regs_cities=[]


#cycle for cities/regions
for i in soup.find_all('a'):
    try:
        if 'magazini/' in i['href']:
            regs_cities.append(i['href'][9:])
    except:
        pass

regs_cities.pop(0)


for i in regs_cities:
    webpage = urllib.request.urlopen(chain_url + i[:len(i)-1])
    soup = BeautifulSoup(webpage, 'lxml')
    for j in soup.find_all('script'):
        j=str(j)
        if 'var points' in j:
            region=re.findall("'region': '(.*?)'", j) #[А-Яа-я ,0-9]\w+
            city_street=re.findall("'title': '(.*?)'", j)
            coords=re.findall("'coords': (\[.*?\])", j)
            addresses['City & Street']+=city_street
            addresses['Region']+=region
            addresses['coords']+=coords
addr=pd.DataFrame(addresses)
addr['City & Street']=addr['City & Street'].str.strip()
addr.drop_duplicates(subset='City & Street', inplace=True)

addr.to_csv(os.curdir+'LitRa addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))