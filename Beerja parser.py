# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:10:19 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "http://beerja.ru/stores.php"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

addresses={'Region':[],'District':[],'City':[],'Street':[]}
#Region=''
#Distr=''
#City=''
for i in soup.find_all(['a','li']):
#    print(i)
    try:
        if 'inner-item' in i['class'][0]: #'/inc/getmap' in i['href'] or 'inner-item' in i['class'][0]
#            print(i)
            Address=i.string
            addresses['Region'].append(Region)
            addresses['District'].append(Distr)
            addresses['City'].append(City)            
            addresses['Street'].append(Address)
        elif '/inc/getmap' in i['href']:
#            print(1)
            Address=i.string
            addresses['Region'].append(Region)
            addresses['District'].append(Distr)
            addresses['City'].append(City)            
            addresses['Street'].append(Address)
        else:
            if 'region-title' in i['class']:
                Region=i.string
                Distr=''
#                continue
            
            elif 'district-title' in i['class']:
                Distr=i.string
#                continue

            elif 'city-title' in i['class']:
                City=i.string
                Distr=''
#             continue

    except:
        pass
addr=pd.DataFrame(addresses)
addr.dropna(subset=['Street'], inplace=True)
addr.to_csv(os.curdir+'BEERja addresses.csv', sep=';', index=False)


#i=soup.find_all('a')[14]
#i['class']
#
#i=soup.find_all('li')[158] #<li class="accordion__inner-item">ул. Куйбышева, 34, м-н «Светофор»</li>
#soup.find_all('a')[168]
end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))