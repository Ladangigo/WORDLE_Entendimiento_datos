# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:26:58 2022

@author: Usuario
"""

with open('uniondearchivos.txt', 'r',encoding="utf8") as raw_file:
    original_file = raw_file.read()

txt = original_file.split(' ')


print(txt)