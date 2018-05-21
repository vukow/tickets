# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 09:57:56 2017

@author: Mario
"""

import urllib2, unicodedata
from bs4 import BeautifulSoup

def tickets(tipo, ciudad="", fecha="", pmin=0, pmax=0):
    url ='https://www.----.com/'+tipo+'?'
    if ciudad:
        url += 'location='+ciudad+'&'
    if fecha:
        url += 'date='+fecha+'&'
    if pmin:
        url += 'min_price='+str(pmin)+'&'
    if fecha:
        url += 'max_price='+str(pmax)+'&'
    
    i = 0
    links=['hola']
    while(not(not links) and i<11):
        url2 = url + 'page=' + str(i)
        conector = urllib2.urlopen(url2)
        htm = conector.read()
        conector.close()    
        soup = BeautifulSoup(htm,'html5')
        links = soup.find_all('article',{'class':'card card--small'})
        i += 1
        
        for tag in links:
            Evento = tag.find('span',{'class':'clip-text'}).get_text(strip=True)
            Fecha = tag.findAll('meta',{'itemprop':'startDate'})
            Precio = tag.findAll('meta',{'itemprop':'lowPrice'})
            Lugar = tag.find('div',{'class':'location__text'})
            Lugar1 = Lugar.find('span',{'itemprop':'name'})
            Lugar2 = Lugar.find('span',{'itemprop':'addressLocality'})

            if Fecha is not None and len(Fecha)>0:
                Fecha = Fecha[0].get("content")
            
            if Lugar1 is not None and len(Lugar1)>0:
                Lugar1 = Lugar1.get_text(strip=True)
            else:
                Lugar1 = "No hay info"  
            
            if Lugar2 is not None and len(Lugar2)>0:
                Lugar2 = Lugar2.get_text(strip=True)
            else:
                Lugar2 = "No hay info"  
     
            normalizado = unicodedata.normalize('NFKD', Evento).encode('ascii','ignore')
            archivo.write(normalizado+'\t')
            archivo.write(Fecha+'\t')
            normalizado=unicodedata.normalize('NFKD', Lugar1).encode('ascii','ignore')
            archivo.write(normalizado+'\t')
            normalizado=unicodedata.normalize('NFKD', Lugar2).encode('ascii','ignore')
            archivo.write(normalizado+'\t')
            
            if Precio is not None and len(Precio)>0:
                Precio = Precio[0].get("content")
                archivo.write((str(Precio).replace(',','.')))
                    
            archivo.write('\n')
        
#Programa principal
print('Comienza el programa')
archivo=open('tickets.csv','w')
archivo.write('Artista \t')
archivo.write('Fecha \t')
archivo.write('Sala \t')
archivo.write('Ciudad \t')
archivo.write('Precio \n')

#El CSV separa las columnas por medio de tabuladores
 
#Ruta de la página web
    
tickets('conciertos')
 
archivo.close()
print('Fin del programa')
