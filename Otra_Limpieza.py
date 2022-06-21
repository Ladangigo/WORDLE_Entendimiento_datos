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


#----------------------Solo letras----------------------------------
file_without_numbers = [ ]
file_without_numbers_changing_accents = [ ]

#Para la limpieza según los lineamientos de limpieza
file_without_numbers = re.findall(r'[aA-zZÑñ]+', textu)

# Para la limpieza cambiando todas las letras con los diferentes tipos de acentos por sus homólogos
file_without_numbers_changing_accents = re.findall(r'[aA-zZÑñ]+', textoc)  
    
#-----------------------Eliminar duplicados------------------------------
file_without_duplicates = [ ]

#Para la limpieza según los lineamientos de limpieza
file_without_duplicates = list(OrderedDict.fromkeys(file_without_numbers)) 

# Para la limpieza cambiando todas las letras con los diferentes tipos de acentos por sus homólogos 
file_without_duplicates_changing_accents = list(OrderedDict.fromkeys(file_without_numbers_changing_accents)) 

#---------------------Elimino stopwprds-------------------------------
file_without_stopwords = []
file_without_stopwords_changing_accents = []

#Para la limpieza según los lineamientos de limpieza
item = None
for item in file_without_duplicates:
  if not item in stop_words:
    file_without_stopwords.append(item)

# Para la limpieza cambiando todas las letras con los diferentes tipos de acentos por sus homólogos 
item = None
for item in file_without_duplicates_changing_accents:
  if not item in stop_words:
    file_without_stopwords_changing_accents.append(item)

#---------------------Eliminar palabras con longitud menores a 4 letras ----------------------
#Para la limpieza según los lineamientos de limpieza
clean_file=file_without_stopwords.copy()
word= None
for word in file_without_stopwords:
  if len(word)<4:
    clean_file.remove(word)  

# Para la limpieza cambiando todas las letras con los diferentes tipos de acentos por sus homólogos
clean_filechanging_accents=file_without_stopwords_changing_accents.copy()
word= None
for word in file_without_stopwords_changing_accents:
  if len(word)<4:
    clean_filechanging_accents.remove(word)  





