# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:54:46 2016

@author: fialdm01
"""
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

start = time.clock()
chain_url = "http://pivomankazan.ru/map.php"
webpage = urllib.request.urlopen(chain_url)
soup = BeautifulSoup(webpage, 'lxml')

#regs=[]

regs_cities = soup.find_all('div', {'id':'choose'})
addr_chars={'Region':[],'City':[],'Link':[]}
addresses = {'Region':[],'City':[],'District':[],'Address':[]}

for j in BeautifulSoup(str(regs_cities), 'lxml').find_all('option'):
#    print(j)
    try:
        if j['value']:
#            pass
#            print(j)
            City=j.string
            Reg_link=str(j['value'])
            addr_chars['Region'].append(Region)
            addr_chars['City'].append(City)
            addr_chars['Link'].append(Reg_link)           
    except:
        Region=j.string #Region находится в except, потому что в else цикл не попадет - ошибка

#addr=pd.DataFrame(addr_chars)

broken_links=[]

for i in range(len(addr_chars['Link'])):
    chain_url = "http://pivomankazan.ru/"+addr_chars['Link'][i]
    try:
        webpage = urllib.request.urlopen(chain_url)
    except:
        pass
        broken_links.append(addr_chars['Link'][i])
    soup = BeautifulSoup(webpage, 'lxml')
    for w in soup.find_all('div', {'class':'view-source'}):
        Distr=''
        for j in BeautifulSoup(str(w),'lxml').find_all(['a','ul']):
            try:
                if j['id']=='raion':
                    Distr=j.string
#                    print(Distr)
            except:
#                print (j)
                try:
                    if j['class']==["parametrs"]: #=='parametrs'
#                        print(j)
                        for q in BeautifulSoup(str(j),'lxml').find_all('p'):
#                            print(q)
#                    if q['class']=='parameters':
#                        for w in BeautifulSoup(q,'lxml').find_all('p'):
                            Address=q.string
                            addresses['Region'].append(addr_chars['Region'][i])
                            addresses['City'].append(addr_chars['City'][i])
                            addresses['District'].append(Distr)
                            addresses['Address'].append(Address)
##                    if j['target']=='newframe':
#    #                    print(1)
#                        Address=j.string
#                        addresses['Region'].append(addr_chars['Region'][i])
#                        addresses['City'].append(addr_chars['City'][i])
#                        addresses['District'].append(Distr)
#                        addresses['Address'].append(Address)
                except:
                    pass
                    
addr=pd.DataFrame(addresses)
addr.to_csv(os.curdir+'Pivoman Kazan addresses.csv', sep=';', index=False)                   
            

#j=soup.find_all('a')[11]
#
#chain_url = "http://pivomankazan.ru/maps/kazanmap.php"
#chain_url = "http://pivomankazan.ru/maps/chistopol.php"





end = time.clock()
print("Программа работала {} секунд.".format(int(end - start)))



#for i in range(len(addr_chars['Link'])):
#    chain_url = "http://pivomankazan.ru/"+addr_chars['Link'][i]
#    try:
#        webpage = urllib.request.urlopen(chain_url)
#    except:
#        pass
#        broken_links.append(addr_chars['Link'][i])
#    soup = BeautifulSoup(webpage, 'lxml')
#    for j in soup.find_all('a'):
#        Distr=''
#        try:
#            if j['id']=='raion':
##                print(j, type(j))
#                Distr=j.string
#            
#        except:
#            try:
#                if j['target']=='newframe':
##                    print(1)
#                    Address=j.string
#                    addresses['Region'].append(addr_chars['Region'][i])
#                    addresses['City'].append(addr_chars['City'][i])
#                    addresses['District'].append(Distr)
#                    addresses['Address'].append(Address)
#            except:
#                pass