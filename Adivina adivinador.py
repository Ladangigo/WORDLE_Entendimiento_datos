# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:35:06 2022

@author: Laura
"""
import pandas as pd
import numpy as np
import requests

class Update_words():
            
    def __init__(self, APIget_response_length,APIget_number_vowels, database, APIpost_response = None):
        self.APIget_response_length = APIget_response_length
        self.APIget_number_vowels = APIget_number_vowels
        self.APIpost_response = APIpost_response
        self.database = database
        self.filter_words_according_APIget()
 
    def filter_words_according_APIget (self):
          self.words_game = self.database.loc[np.logical_and(self.database['Longitud'] == int(self.APIget_response_length),
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
    
    def __init__(self, database):
        self.database_game = database
        
        
    def calculate_pattern(self):
          word_length = len(self.database_game['Palabra'][0])

          newDF_dict = {'Palabra':[]}
          for newKey in range(word_length):
            newDF_dict[f'posicion {str(newKey)}'] = [ ]
          
          for index, length in enumerate(self.database_game['Palabra']):
            word = self.database_game['Palabra'][index]
            newDF_dict['Palabra'].append(word)
        
            for positionVowel in self.database_game['posicionVocal'][index]:
              newDF_dict[f'posicion {str(positionVowel)}'].append(1)#1 para vocales
            for positionCons in self.database_game['posicionCons'][index]:
              newDF_dict[f'posicion {str(positionCons)}'].append(0)#0 para Consonante
        
          self.words_patterns = pd.DataFrame(newDF_dict)
        
    # Se selecciona el patrón con mayor incidencia       
    def select_pattern(self):
          resume_patterns = self.words_patterns[self.words_patterns.columns[1:]].groupby(
              self.words_patterns[self.words_patterns.columns[1:]].columns.tolist(),as_index=False).size()
  
          pattern_more_often = resume_patterns['size'].max()
        
          filter_pattern=resume_patterns['size']==pattern_more_often
          positions = np.flatnonzero(filter_pattern)
          higher_incidence_pattern = resume_patterns.iloc[positions]
          
          select_patterns_higher_incidence = self.words_pattern.join(higher_incidence_pattern.set_index(list(higher_incidence_pattern.columns.values[:-1])), 
                                        on=list(self.words_pattern.columns.values[1:]), how='right')
          self.words_select_patterns_higher_incidence = list(select_patterns_higher_incidence['Palabra'].values)
          
          
    def probabilities_letter_in_position(self):
        pass

       
class Game():
    
    def __init__(self,database):
        self.getAPI_communication()

        
        self.choose_words = Update_words(self.word_length, self.number_vowels, database)
        
    def getAPI_communication(self):
        response = requests.get('http://localhost:5000/getword')
        dictionary = response.json()
        print(dictionary, type(dictionary))
        self.word_length = dictionary['Longitud']
        self.number_vowels = dictionary['Cant Vocales']
    

class Sistem():
    
    def __init__(self):
       
        self.open_file()
        self.position_vowels_cons()
        
        
        
    def open_file(self):
        self.words_bank = [ ]
        with open("final_cleanLaura.txt", 'r', encoding='utf8') as words:
              word_bank = words.read()
        self.words_bank = word_bank.split(' ')
        
    def position_vowels_cons(self):
        dictToDF_wordInfo = {'Palabra':[],'Consonante':[],'posicionCons': [], 'Vocal':[],'posicionVocal':[], 'Longitud': []}
        vowels =[]
        cons = []
        
        #Conocer el numero de vocales y consonantes de una palabra
        for word in self.words_bank:
          numberVowels = len([l for l in word if l in 'aeiou'])
          numberCons = len(word) - numberVowels
          length = len(word)
          dictToDF_wordInfo['Palabra'].append(word)
          dictToDF_wordInfo['Consonante'].append(numberCons)
          dictToDF_wordInfo['Vocal'].append(numberVowels)
          dictToDF_wordInfo['Longitud'].append(length)
          
          for position,letter in enumerate(word):
            if letter in 'aeiou':
              vowels.append(position)
            else:
              cons.append(position)
                
          dictToDF_wordInfo['posicionVocal'].append(vowels)
          dictToDF_wordInfo['posicionCons'].append(cons)
          vowels =[]
          cons = []
        
        self.DF_wordInfo = pd.DataFrame(dictToDF_wordInfo)
        
    def configure_game(self):
        self.game = Game(self.DF_wordInfo)


a = Sistem()

a.configure_game()
#a.game.choose_words.words_game