# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:30:26 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()
chain_url = "http://www.ircenter.ru/ru/company_34522_%D0%9A%D0%9B%D0%90%D0%A1%D0%A1-%D0%9C%D0%90%D0%A0%D0%9A%D0%95%D0%A2-%D1%81%D0%B5%D1%82%D1%8C-%D1%81%D1%83%D0%BF%D0%B5%D1%80%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%BE%D0%B2"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

addresses = {'Address':[]}

for i in soup.find_all('td'):
    if 'Адрес :' in i.text:
        for j in re.findall('<b>Адрес : <\/b>([0-9A-Яа-я,.\- \/]+)</td></tr><tr',str(i)):
            address=j
            addresses['Address'].append(address)
        #print(address)

addr=pd.DataFrame(addresses)
addr.drop_duplicates(inplace=True)

#addr = pd.DataFrame(addr.row.str.split(', ',1).tolist(),columns = ['post code','City','District','Street','address'])

addr.to_csv(os.curdir+'Class Market addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))