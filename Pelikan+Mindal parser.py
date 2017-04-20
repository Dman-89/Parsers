# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:51:35 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "https://neo63.ru/address.php"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

cities={'City':[], 'Link':[]}
addresses={'City':[],'Address':[]}

for i in soup.find_all('a'):
    try:
        if 'address.php?group' in i['href']:
            cities['City'].append(str(i.string))
            cities['Link'].append(i['href'][11:])
    except:
        pass
            
for i in range(len(cities['Link'])):
    try:
        chain_url = "https://neo63.ru/address.php"+cities['Link'][i]
        webpage = urllib.request.urlopen(chain_url)
        soup = BeautifulSoup(webpage, 'lxml')
        for j in soup.find_all('a'):
            try:
                if j['target']=='_blank': #"П" in j['title']:
                    addresses['City'].append(cities['City'][i])
                    addresses['Address'].append(str(j.string))
            except:
                pass
#                print(0)
    except:
        print('error in '+cities['Link'][i])


addresses['CHA']=['PEI' for i in range(len(addresses['Address']))]
#addresses['District']=['' for i in range(len(addresses['Address']))]

#mindal part
chain_url = "http://www.mindalmarket.ru/pages/adresa_magazinov2/"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

for i in soup.find_all(['h1','p']):
    if '<h1' in str(i):
        City=i.string
#        print(City)
    elif '<br/>' in str(i) and '(карта проезда в главный офис)' not in str(i): # '<p>' in str(i) and
#        Address=i.text
        Address=str(i)[str(i).find('<p>')+3:str(i).find('<br/>')]
        addresses['City'].append(str(City))
        addresses['Address'].append(str(Address))
        addresses['CHA'].append('MND')
#        print(Address)


addr=pd.DataFrame(addresses)

addr.to_csv(os.curdir+'Pelikan+Mindal addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))