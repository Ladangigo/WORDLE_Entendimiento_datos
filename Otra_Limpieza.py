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
    
def change_all_accents(file):
    letters_with_accents = ((r'á','a'),(r'é','e'),(r'í','i'),(r'ó','o'),(r'ú','u'),
              (r'ä','a'),(r'ë','e'),(r'ï','i'),(r'ö','o'),(r'ü','u'),
              (r'ý','y'),(r'ś','s'),(r'ć','c'))

    for i in letters_with_accents:
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
    

#Proceso de limpieza estipulada por el cliente

# 1. Se eliminan caracteres
remove_characters = delete_symbols(raw_file_join)

# 2. Se eliminan palabras con mas de 2 letras en mayúsculas
del_uppcase = delete_uppcase(remove_characters)

# 3. Se pasa todo de mayúsculas a minúsculas
change_letters_to_lowercase = convert_uppercase_to_lowercase(del_uppcase)

# 4. Se cambian las vocales con tíldes por sus homólogas sin ellas
change_accentsvowels = change_accents(change_letters_to_lowercase)

# 5. Se eliminan numeros y otros caracteres, quedando solo letras
only_letters = filter_only_letters(change_accentsvowels)

# 6. Se eliminan duplciados
delete_duplicates = remove_duplicates(only_letters)

# 7. Se eliminan las stop words
remove_stopwords = delete_stopwords(delete_duplicates)

# 8. se eliminan las palabras que tengan menos de 4 letras
delete_words_less_than_four = delete_words(remove_stopwords)

#Información sobre el total de palabras del banco 
total_words = len(delete_words_less_than_four)
print (f"Se cuenta con un total de {total_words} palabras")


# Proceso de limpieza caso 1: Se reemplazan todas las letras con acentos por sus homólogos sin ellas

# 4. Se cambian todos los acentos
change_accentsletters = change_all_accents(change_letters_to_lowercase)

# 5. Se eliminan numeros y otros caracteres, quedando solo letras
only_letters_with_accents = filter_only_letters(change_accentsletters)

# 6. Se eliminan duplciados
delete_duplicates_with_accents = remove_duplicates(only_letters_with_accents)

# 7. Se eliminan las stop words
remove_stopwords_with_accents = delete_stopwords(delete_duplicates_with_accents)

# 8. se eliminan las palabras que tengan menos de 4 letras
delete_words_less_than_four_with_accents = delete_words(remove_stopwords_with_accents)

#Información sobre el total de palabras del banco con el cambio realizado
total_words_with_accents = len(delete_words_less_than_four_with_accents)
print (f"Al cambiar todos las letras que tienen acentos por sus homólogos se cuenta con un total de {total_words_with_accents} palabras")










