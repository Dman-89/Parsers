# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:55:16 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "http://www.gorilka63.ru/shops"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

addresses = {'Region':[],'City':[],'Address':[]}

for i in soup.find_all('div'):
    try:
        if 'tree-item-title' in i['class']:
            Region=i.text
        elif 'tree-item-children-title' in i['class']:
            City=i.text
        elif 'tree-item-children-item-goods' in i['class']:
            Address=i.text
            addresses['Region'].append(Region)
            addresses['City'].append(City)
            addresses['Address'].append(Address)
    except:
        pass

addr=pd.DataFrame(addresses)

#addresses['Region']=[i.strip('\n') for i in addresses['Region']]
#addresses['City']=[i.strip('\n') for i in addresses['City']]
#addresses['Address']=[i.strip('\n') for i in addresses['Address']]

addr['Region']=addr['Region'].str.strip('\n')
addr['City']=addr['City'].str.strip('\n')
addr['Address']=addr['Address'].str.strip('\n')

addr.to_csv(os.curdir+'Gorilka addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))
