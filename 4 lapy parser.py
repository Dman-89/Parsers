# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:51:40 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()

chain_url = "http://4lapy.ru/pet_stores_amp_services/"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

addresses = {'Address':[],'City':[],'coords':[]}

for i in soup.find_all('script',{'type':'text/javascript'}):
    if len(re.findall("myClusterer\.add\(new ymaps\.Placemark\(\[([0-9., ]+)\]", str(i)))>50:
        addresses['coords']=re.findall("myClusterer\.add\(new ymaps\.Placemark\(\[([0-9., ]+)\]", str(i))
        addresses['City']=re.findall('<h3 class="name"><span>([ёА-Яа-я \-]+)</span></h3>', str(i))
#    Cities1=re.findall('<h3 class="name"><span>(.+)</span></h3>', str(i))
        addresses['Address']=re.findall('<div class="adress"><div>(.+)</div></div>', str(i)) #&quot;
        addresses['Address']=[i.replace('&quot;','"') for i in addresses['Address']]        

#for i in addresses['Address']:
#    i.replace('&quot;','"')
#    print(i)
        
#i=soup.find_all('script',{'type':'text/javascript'})[27]

addr=pd.DataFrame(addresses)

addr.to_csv(os.curdir+'4Lapy addresses.csv', sep=';', index=False)

end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))