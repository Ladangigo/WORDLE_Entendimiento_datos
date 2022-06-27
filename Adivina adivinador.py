# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:35:06 2022

@author: Laura
"""

class Update_words():
            
    def __init__(self, APIget_response_length, database, APIpost_response = None):
        self.APIget_response_length = APIget_response_length
        self.APIpost_response = APIpost_response
        self.database = database
 
    def filter_words_according_APIget (self):
          self.words_game = [ ]
          self.words_game = self.database[str(self.APIget_response_length)]
        
        
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
    pass
