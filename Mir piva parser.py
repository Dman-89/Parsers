# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:14:41 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "http://mir-piva.com/network.php"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

cities={'City':[], 'Nr':[]}

addresses={'City':[],'Address':[]}

for i in soup.find_all('a'):
    try:
        if i['data-id']:
            if not BeautifulSoup(str(i), 'lxml').find('span'):
                cities['City'].append(str(i.string))
                cities['Nr'].append(i['data-id'])
    except:
        pass

for i in range(len(cities['Nr'])):
    try:
        for j in soup.find_all('ul',{'data-id': cities['Nr'][i]}):
            x=BeautifulSoup(str(j), 'lxml').find_all('span')
            for q in x:
                addresses['City'].append(str(cities['City'][i]))
                addresses['Address'].append(str(q.string))
    except:
        print('error in '+j)

addr=pd.DataFrame(addresses)

addr.to_csv(os.curdir+'Mir piva addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))