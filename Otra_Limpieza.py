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
    
    
def delete_stopwords(file):
    file_without_stopwords = [ ]
    for item in file:
      if not item in stop_words:
        file_without_stopwords.append(item)
    return file_without_stopwords
    

def delete_words(file):
    clean_file=file.copy()
    word= None
    for word in file:
      if len(word)<4:
        clean_file.remove(word) 
    return clean_file
    

def convert_uppercase_to_lowercase(file):
    file_lowercase = [ ]
    file_lowercase = file.lower() # convertir mayus en minusculas
    return file_lowercase
    
def remove_duplicates(file):
    file_without_duplicates = [ ]
    file_without_duplicates = list(OrderedDict.fromkeys(file)) 
    return file_without_duplicates
    

#Proceso de limpieza

remove_characters = delete_symbols(raw_file_join)
del_uppcase = delete_uppcase(remove_characters)
change_letters_to_lowercase = convert_uppercase_to_lowercase(del_uppcase)
change_accentsvowels = change_accents(change_letters_to_lowercase)
only_letters = filter_only_letters(change_accentsvowels)
delete_duplicates = remove_duplicates(only_letters)
remove_stopwords = delete_stopwords(delete_duplicates)
delete_words_less_than_four = delete_words(remove_stopwords)

#Recopilación de datos para un posterior analisis estadistico 
Total_palabras = len(delete_words_less_than_four)
print (f"Se cuenta con un total de {Total_palabras} palabras")














