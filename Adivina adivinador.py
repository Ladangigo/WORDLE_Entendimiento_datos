# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:35:06 2022

@author: Laura
"""
import pandas as pd
import numpy as np

class Update_words():
            
    def __init__(self, APIget_response_length,APIget_number_vowels, database, APIpost_response = None):
        self.APIget_response_length = APIget_response_length
        self.APIget_number_vowels = APIget_number_vowels
        self.APIpost_response = APIpost_response
        self.database = database
        self.filter_words_according_APIget()
 
    def filter_words_according_APIget (self):
          self.words_game = self.database.loc[np.logical_and(self.database['longitud'] == int(self.APIget_response_length),
                                                             self.database['Vocal'] == int(self.APIget_number_vowels))]
          
          
        
        
    def filter1():
        pass
    
    def filter2():
        pass
    
    def filter3():
        pass
           
    
    def update_APIpost():
        pass

   

class Select_words():
    pass

class Game():
    pass

class Sistem():
    
    def __init__(self, route):
        self.route = route
        
    def open_file(self, route):
        self.words_bank = [ ]
        with open(route, 'r', encoding='utf8') as words:
              word_bank = words.read()
        self.words_bank = word_bank.split(' ')
        
    def position_vowels_cons(self):
        dictToDF_wordInfo = {'Palabra':[],'Consonante':[], 'Vocal':[], 'Longitud': []}

        #Conocer el numero de vocales y consonantes de una palabra
        for word in self.words_bank:
          numberVowels = len([l for l in word if l in 'aeiou'])
          numberCons = len(word) - numberVowels
          length = len(word)
          dictToDF_wordInfo['Palabra'].append(word)
          dictToDF_wordInfo['Consonante'].append(numberCons)
          dictToDF_wordInfo['Vocal'].append(numberVowels)
          dictToDF_wordInfo['Longitud'].append(length)
        
        self.DF_wordInfo = pd.DataFrame(dictToDF_wordInfo)

