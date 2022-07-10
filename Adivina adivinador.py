# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:35:06 2022

@author: Laura
"""
import pandas as pd
import numpy as np
import requests
import time

class Update_words():
            
    def __init__(self, APIget_response_length,APIget_number_vowels, database, APIpost_response = None):
        self.actualWord = None
        self.APIget_response_length = APIget_response_length
        self.APIget_number_vowels = APIget_number_vowels
        self.APIpost_response = APIpost_response
        self.database = database
        self.filter_words_according_APIget()
 
    def filter_words_according_APIget (self):
        # Filtra la base de datos segun la longitud de la palabra y cantidad de vocales según
        # respuesta de API GET
        self.words_game = self.database.loc[np.logical_and(self.database['Longitud'] == int(self.APIget_response_length),
                                                             self.database['Vocal'] == int(self.APIget_number_vowels))]
          
          
    def organize_database_to_filter(self):
        # Organiza la base de datos por palabra y la posición de la letra que ocupa en cada palabra

        word_length = len(self.words_game.iloc[0]['Palabra'])
        
        words_letter_position = {'Palabra':[]}
        for newKey in range(word_length):
          words_letter_position[f'posicion{str(newKey)}'] = [ ]  
        
        for index, length in enumerate(self.words_game['Palabra']):
          

          words_letter_position['Palabra'].append(length)
        
        
          for position, letter in enumerate(length):
            words_letter_position[f'posicion{str(position)}'].append(letter)
        print(len(words_letter_position['Palabra']))
        
        self.words_game = pd.DataFrame(words_letter_position)
    
        
        
    def filter1(self): 
        # Elimina las palabras que tengan la letra en la posición equivocada

        print('---FILTRO 1')

        # Aplico filtro
        for i in self.letters_position_f1:
          indexNames = self.words_game[self.words_game[i[0]] == i[1]].index
          self.words_game.drop(indexNames,inplace=True)

          
        print(self.words_game)
        
   
    def organize_info_apipost(self):
        # Se organiza la información entregada por API post relevante para filtro 2 y 3
        print('---FILTRO APIPOST')
        
        
        self.correct_letters = self.APIpost_response['right_letters_in_wrong_positions']
        word_sent_APIpost = self.actualWord
        correct_letters_boolenao = self.APIpost_response['position_array']
        print(self.actualWord)
        word_sent_APIpost  = self.actualWord
        word_send = list(word_sent_APIpost)

        
        count = 0
        letters_correct = [ ]
        self.letters_correct_position = [ ]
        tuple_letter_position = [ ]
        Letters_part_word = [ ]
        
        self.letters_position_f1 = []
        letter_position_1 = [ ]
        
        for tuple_letter in zip(correct_letters_boolenao, word_send):
          if tuple_letter[0] == True:
              letters_correct.append(tuple_letter[1])
              tuple_letter_position.append(tuple_letter[1])
              tuple_letter_position.append(f'posicion{count}')
              self.letters_correct_position.append(tuple_letter_position)
              tuple_letter_position = [ ]
          else:
              letter_position_1.append(f'posicion{count}')
              letter_position_1.append(str(tuple_letter[1]))
              self.letters_position_f1.append(letter_position_1)
              letter_position_1 = [ ]
            
        
          count += 1
        
        Letters_part_word = letters_correct + self.correct_letters
        self.Letters_remove = list(set(word_send).difference(set(Letters_part_word)))

        
        
        print(self.words_game)
        print(self.letters_correct_position)
        print(self.Letters_remove)

   
         
    def filter2(self):
        # eliminar las palabras que tengan las letras que no hacen parte de mi palabra de busqueda 
        print('---FILTRO 2')
        # construir la lista de las letras que no están presentes 
        for column in self.words_game.columns:
          for letter in self.Letters_remove:
            indexNames = self.words_game[self.words_game[column] == letter].index
            self.words_game.drop(indexNames,inplace=True)
        print(self.words_game)
        
    
    
    def filter3(self):
        # fijar posiciones que si estan correctas
        print('---FILTRO 3')
        print(self.letters_correct_position)
        for i in self.letters_correct_position:
            
            self.words_game = self.words_game.query(f'{i[1]} == "{i[0]}"')

        print(self.words_game)
           
    
    def update_APIpost(self, postApi_response):
        # Actualiza la respuesta de la APIpost, despues de haber enviado una palabra
        self.APIpost_response = postApi_response
        memorys = [ ]
        memorys.append(self.APIpost_response)
        print(f'se a almacenado en la memoria del juego {memorys}')
    


class Select_words():
    
    def __init__(self, database):
        self.actualWord = None
        self.database_game = database
        self.calculate_pattern()
        self.select_pattern()
        self.frecuency_letter_in_position()
        self.select_words_more_often()
        self.letter_in_position()
        
        
        
    def calculate_pattern(self):
        self.database_game = self.database_game.reset_index()
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
        
          
    def select_pattern(self):
        # Se selecciona el patrón con mayor incidencia 
          resume_patterns = self.words_patterns[self.words_patterns.columns[1:]].groupby(
              self.words_patterns[self.words_patterns.columns[1:]].columns.tolist(),as_index=False).size()
  
          pattern_more_often = resume_patterns['size'].max()
        
          filter_pattern=resume_patterns['size']==pattern_more_often
          positions = np.flatnonzero(filter_pattern)
          higher_incidence_pattern = resume_patterns.iloc[positions]
          
          select_patterns_higher_incidence = self.words_patterns.join(higher_incidence_pattern.set_index(list(higher_incidence_pattern.columns.values[:-1])), 
                                        on=list(self.words_patterns.columns.values[1:]), how='right')
          self.words_select_patterns_higher_incidence = list(select_patterns_higher_incidence['Palabra'].values)
          
          
    def frecuency_letter_in_position(self):
        # Calcula la frecuencia de las letras en posición de la palabra
        letterPosition = {'Letra':[], 'Posicion':[]}
        
        for word in self.words_select_patterns_higher_incidence:
            for position4,letter4 in enumerate(word):    
              letterPosition['Letra'].append(letter4)
              letterPosition['Posicion'].append(position4)
            
        
        self.DF_letterPosition = pd.DataFrame(letterPosition)
        self.table_of_frecuency = pd.crosstab(self.DF_letterPosition['Letra'], self.DF_letterPosition['Posicion'])
        
     
        amount_colum = len(self.table_of_frecuency.columns.values)
        positions = [ ]
        for i in range(amount_colum):
            positions.append(f'Posicion{str(i)}')
          
        self.tablefrecuency = self.table_of_frecuency.set_axis(positions,axis=1)
        
    def select_words_more_often(self):
        
        self.column_criterion = [[],[],[]]
        letter_most_often = self.tablefrecuency['Posicion0'].max()
        filtered_df = self.tablefrecuency.query(f'Posicion0 == {str(letter_most_often)}')
        letter_select = filtered_df.axes[0][0]
        self.column_criterion[0].append('Posicion0')
        self.column_criterion[1].append(letter_select)
        self.column_criterion[2].append(letter_most_often)
        
        for i, column in enumerate(self.tablefrecuency.columns.values):
          count = np.count_nonzero(self.tablefrecuency[column]==0)
          letter_most_often = self.tablefrecuency[column].max()
          if count>=18:
            filtered_df = self.tablefrecuency.query(f'{column} == {str(letter_most_often)}')
            letter_select = filtered_df.axes[0][0]
            if letter_select in self.column_criterion[1]:
              if self.column_criterion[2][self.column_criterion[1].index(letter_select)] < letter_most_often:
                self.column_criterion[0][self.column_criterion[1].index(letter_select)]=column
                self.column_criterion[1][self.column_criterion[1].index(letter_select)]=letter_select
                self.column_criterion[2][self.column_criterion[1].index(letter_select)]=letter_most_often 
            else:
              self.column_criterion[0].append(column)
              self.column_criterion[1].append(letter_select)
              self.column_criterion[2].append(letter_most_often)
        
    
    def letter_in_position(self):
        word_length = len(self.database_game['Palabra'][0])
        
        letter_position_dic = {'Palabra':[]}
        for newKey in range(word_length):
          letter_position_dic[f'posicion{str(newKey)}'] = [ ]  
        
        for index, length in enumerate(self.database_game['Palabra']):
          
          word = self.database_game['Palabra'][index]
          
          letter_position_dic['Palabra'].append(word)
        
        
          for position, letter in enumerate(length):
            letter_position_dic[f'posicion{str(position)}'].append(letter)
     
        
        self.dfletter_position = pd.DataFrame(letter_position_dic)
               
  
    def select_initial_word(self):

        self.df_letter_position = self.dfletter_position.copy()

        for i in range(len(self.column_criterion[0])):
          print(self.column_criterion[0][i], self.column_criterion[1][i])
          boolean = self.df_letter_position[self.column_criterion[0][i].lower()]==self.column_criterion[1][i]
          self.df_letter_position = self.df_letter_position[boolean] 
        
        word = [len(set(possible_selected_word)) for possible_selected_word in self.df_letter_position['Palabra'].tolist()]
        print(word.index(max(word)))
        word_select = self.df_letter_position.iloc[word.index(max(word)), 0]
        self.actualWord = word_select
    
    def select_word(self, dataBaseFiltered):
        self.actualWord = dataBaseFiltered.sample().iloc[0,0]
        print('Palabra escogida: ', self.actualWord)
       
class Game():
    
    def __init__(self,database):

        self.memory = [ ]
        self.getAPI_communication()
        
        self.choose_words = Update_words(self.word_length, self.number_vowels, database)
        
        self.selec_word = Select_words(self.choose_words.words_game)
        
        self.selec_word.select_initial_word()
        
        self.postAPI_communication()
        
    def getAPI_communication(self):
        response = requests.get('https://7b8uflffq0.execute-api.us-east-1.amazonaws.com/game/get_params', auth = ('laura.gil','8708facdef944079998bdd91018c5ecc'))
        #response = requests.get('http://localhost:5000/getword')
        dictionary = response.json()
        print(dictionary, type(dictionary))
        self.word_length = dictionary['length_word']
        self.number_vowels = dictionary['vowels']
        self.id = dictionary['id']
    
    def postAPI_communication(self):
        palabra_enviar = self.selec_word.actualWord
        self.t2 = time.time() #Antes de la peticion
        response = requests.post('https://7b8uflffq0.execute-api.us-east-1.amazonaws.com/game/check_results', auth = ('laura.gil','8708facdef944079998bdd91018c5ecc'),  json={"result_word": palabra_enviar})
        #response = requests.post('http://localhost:5000/compare', json={"palabra": palabra_enviar})
        self.t3 = time.time() #Despues de la peticion
        print('Palabra enviada: ', palabra_enviar)
        print(response.json())
        self.diccionarioRespuesta = response.json()
        self.score = self.diccionarioRespuesta['score']
        self.diccionarioRespuesta['custom_try_time'] = self.t3 - self.t2
        self.diccionarioRespuesta['id'] = self.id
        self.memory.append(self.diccionarioRespuesta)
        #print(f'La informacion guardada en memoria es {self.memory}')
        #self.memorygame = "".join(self.memory)
        
    def memory_game(self):
        temporalString = ''
        with open('historialdejuegos.txt', 'r', encoding='utf8') as file:
            temporalString = file.read()
            
        with open('historialdejuegos.txt', 'w', encoding='utf8') as file:
            actualInfo = "*".join([str(element) for element in self.memory])
            file.write(temporalString + actualInfo)
        
        
    def adivinando(self):
        self.choose_words.update_APIpost(self.diccionarioRespuesta)
        self.choose_words.actualWord = self.selec_word.actualWord
        self.choose_words.organize_database_to_filter()
        self.choose_words.organize_info_apipost()
        self.choose_words.filter1()
        self.choose_words.filter2()
        self.choose_words.filter3()
        self.selec_word.select_word(self.choose_words.words_game)
        self.postAPI_communication()
        

class Sistem():
    
    def __init__(self):
        self.t1 = time.time() #Momento de inicio
        self.open_file()
        self.position_vowels_cons()
        self.attempts = 0
        
        
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
    
    def time_game(self):
        delta = self.t2 - self.t1
        output = {'id': self.game.id, 'time_game': delta}
        temporalString = ''
        with open('tiempodejuegos.txt', 'r', encoding='utf8') as file:
            temporalString = file.read()
            
        with open('tiempodejuegos.txt', 'w', encoding='utf8') as file:
            file.write(temporalString + '*' + str(output))
    
    
    def run(self):
        
        while True:
            self.game.adivinando()
            print('PUNTUACION: ', self.game.score)
            if self.game.score == 1:
                print('GANO!!')
                break
            else:
                self.attempts += 1
            if self.attempts ==6:
                print('Perdiste')
                break
            #input('Ingrese enter para enviar nueva palabra...')
        self.t2 = time.time() #Momento de Finalizacion
        self.time_game()
        self.game.memory_game()
        
a = Sistem()

a.configure_game()
a.run()
