# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:26:58 2022

@author: Usuario
"""

import re
from collections import OrderedDict
import nltk
from nltk.corpus import stopwords
import os
nltk.download('stopwords')
stop_words = stopwords.words('spanish')


files = []


list_of_files = os.listdir("raw_texts/")

#Se unen todos los archivos en uno solo 
for file in list_of_files:
    with open('raw_texts/' + file, 'r', encoding='utf8') as rawfile:
        raw_files = rawfile.read()
        files.append(raw_files)

        
with open('uniondearchivos.txt', 'w', encoding='utf8') as f: #Se crea un archivo dondese van a unir todos los .txt
    f.write(''.join(files))
    

with open('uniondearchivos.txt', 'r', encoding='utf8') as file: #Se abre el archivo donde estan todos los .txt unidos
    raw_file_join = file.read()
     
    

symbols = ['¿','?','~','`','!','¡','@','#','$','%','^','*','(',')','_','-','+','=','{','}','[',']','\\',':',';','<','>','/', '.', ',','&','\r','\t','\n', '|', '“', '"', '–', '”', '©', '-', '—','…', ';', '‘','’',"'",'\xa0']
for char in symbols:
  raw_file_join = raw_file_join.replace(char,' ')


#Elimino las palabras que contengan mas de dos mayúsculas
delete_uppcase1 = re.sub(r'([A-Z]\w+[A-Z]\w+)',"", raw_file_join)
delete_uppcase2 = re.sub(r'[A-Z]{2,}','',delete_uppcase1)   

#cambia todo a minúsculas 
file_lowercase = delete_uppcase2.lower() 

#cambio acentos
text_without_digits = re.sub(r"á","a", file_lowercase)
texte = re.sub(r"é","e", text_without_digits)
texti = re.sub(r"í","i", texte)
texto = re.sub(r"ó","o", texti)
textu = re.sub(r"ú","u", texto)
#Se cambian todos los acentos diferentes a las tildes por sus homólogos 
textoa1 = re.sub(r"ä","a", textu)
textoe1 = re.sub(r"ë","e", textoa1)
textoi1 = re.sub(r"ï","i", textoe1)
textoo1 = re.sub(r"ö","o", textoi1)
textou1 = re.sub(r"ü","u", textoo1)
textoy = re.sub(r"ý","y", textou1)
textos = re.sub(r"ś","s", textoy)
textoc = re.sub(r"ć","c", textos)


    
    