# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:26:58 2022

@author: Usuario
"""

import random
import os
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
    r_file = file.read()
    raw_file_join = r_file.split(' ')
    
    
    