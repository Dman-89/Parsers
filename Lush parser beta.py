# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:22:44 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "https://www.lushrussia.ru/about/shops/"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

addresses = {'Address':[],'City':[]}#,'coords_x':[],'coords_y':[]
regs_cities=[]
city_names=[]

#cycle for cities/regions
for i in soup.find_all('a',{'class':'vacancies_city'}):
    try:
        if '/about/shops/' in i['href']:
            regs_cities.append(i['href'][13:])
            city_names.append(i.string)
    except:
        pass

regs_cities.pop(0)
city_names.pop(0)


for i in range(len(regs_cities)):
    webpage = urllib.request.urlopen(chain_url + regs_cities[i][:len(regs_cities[i])])
    soup = BeautifulSoup(webpage, 'lxml')
    for j in soup.find_all('div'):
        try:            
            if j['rel']:
                for q in j.find_all('span', {'class':'name'}):
                    addresses['Address'].append(q.string)
                    addresses['City'].append(city_names[i])
        except:
            pass


addr=pd.DataFrame(addresses)

addr.to_csv(os.curdir+'Lush addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))