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
     
    

def delete_symbols(file):    
    symbols = ['¿','?','~','`','!','¡','@','#','$','%','^','*','(',')','_','-','+','=','{','}','[',']','\\',':',';','<','>','/', '.', ',','&','\r','\t','\n', '|', '“', '"', '–', '”', '©', '-', '—','…', ';', '‘','’',"'",'\xa0']
    for char in symbols:
      file = file.replace(char,' ')      
    return file
    

def delete_uppcase(file):
    delete_uppcase1 = re.sub(r'([A-Z]\w+[A-Z]\w+)',"", file)
    delete_uppcase2 = re.sub(r'[A-Z]{2,}','',delete_uppcase1)  
    return delete_uppcase2

    
def change_accents(file):
    vowels = ((r'á','a'),(r'é','e'),(r'í','i'),(r'ó','o'),(r'ú','u'))

    for i in vowels:
      file = re.sub(i[0],i[1], file)
    return file
    
    
def filter_only_letters(file):
    file_without_numbers = [ ]
    file_without_numbers = re.findall(r'[aA-zZÑñ]+', file)
    return file_without_numbers
    
    








file_lowercase = file.lower() # convertir mayus en minusculas

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





