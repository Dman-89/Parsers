# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:27:39 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()
chain_url = "http://stanciya-napitkov.ru/index.php/2013-11-08-11-53-34"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')
addresses = {'Address':[],'Distr':[]}

for i in soup.find_all(['section']):
    Distr=i.find('h3').string
    for j in i.find_all('p'): #i.prettify(formatter='unicode') - ==str() \\\\em.extract().
        print(j)
        Address=str(j.text)
        Address=Address[:Address.find(re.findall('((\+7|7|8)([0-9 \-]){10,})',Address)[0][0])] #доделать регекс!!!
        addresses['Distr'].append(Distr)
        addresses['Address'].append(Address)

addr=pd.DataFrame(addresses)
addr['Address']=addr['Address'].str.strip()
addr.to_csv(os.curdir+'Stanciya napitkov addresses.csv', sep=';', index=False)



#Address1=str(Address[:Address.find('8-')].strip())
#Address2=Address[:Address.find(re.findall('[.\d\-.\d{3}.*]+',Address))]
#
#i=soup.find_all(['section'])[1]
##i.find_all('p')
#i=soup.find_all(['h3','p'])[0]
#
#re.findall('(((8|\+7)[- ]?)?\(?\d{3,5}\)?[- ]?\d{1}[- ]?\d{1}[- ]?\d{1}[- ]?\d{1}[- ]?\d{1}((-?\d{1})?[- ]?\d{1,2})?)',Address)
#re.findall('((\+7|7|8)([0-9 \-]){10,})',Address)
#line='    Bataisk, str. Uritskogo 5        8-918-852-50-47 '
#q=re.findall('((\+7|7|8)([0-9 \-]){10,})',line)




end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))