#Se importan las librerías
import re
from collections import OrderedDict
import nltk
from nltk.corpus import stopwords
import os
nltk.download('stopwords')
stop_words = stopwords.words('spanish')

file_with_uppercase = []
file_without_uppercase = []
dic_files = {}
final_resume_file = []
resume_file = []

def CleanData(namefile):
    #namefile ---> ruta del archivo al cual se realizá el proceso de limpieza
    # CleanData: Hace un proceso de limpieza a cada uno de los archivos que estan en la carpeta "raw_texts/" 
    # que consisite en los siguientes pasos:
    #1.Elimina todos los carácteres o síbolos
    #2. 
    #3.Se eliminan los dígitos númericos 
    #4. Se eliminan siglas, numeros romános y palabra que contengan mas de dos letras en mayúsculas
    #5. Se eliminan palabras duplicadas 
    #6. Se eliminan palabras con una longitud menor a 3
    #Una vez realizado todo este proceso de limpieza de datos, se crea una carpeta la cual 
    # contendrá cada uno de los archivos aquí procesados
    #La función retorna una lista que contiene las palabras válidas para ser parte del 
    # banco de palabras de cada .txt

    
    with open(namefile, 'r',encoding="utf8") as raw_file:
        original_file = raw_file.read()
        
    
    #Eliminar símbolos
    symbols = ['¿','?','~','`','!','¡','@','#','$','%','^','*','(',')','_','-','+','=','{','}','[',']','\\',':',';','<','>','/', '.', ',','&','\r','\t', '|', '“', '"', '–', '”', '©', '-', '—','…', ';', '‘','’']
    for char in symbols:
        original_file = original_file.replace(char,' ')

    #Elimino las palabras que contengan mas de dos mayúsculas
    delete_uppcase1 = re.sub(r'([A-Z]\w+[A-Z]\w+)',"", original_file)
    delete_uppcase2 = re.sub(r'[A-Z]{2,}','',delete_uppcase1)
        
    
    
                                
    #convierto la lista en un srt
    file_without_uppercase_str = " ".join(file_without_uppercase)
    
    #cambia todo a minúsculas 
    file_lowercase = file_without_uppercase_str.lower()  

    file_with_stopwords = re.findall(r'[aA-zZñÑ]+', file_lowercase)
      
    
    #Elimino los stop words
    file_without_stopwords = []
    for item in file_with_stopwords:
        if not item in stop_words:
            file_without_stopwords.append(item)
    
    #Elimino palabras duplicadas
    file_without_duplicates = list(OrderedDict.fromkeys(file_without_stopwords))
    
    #Elimino las palabras con lingitud menor a 4
    short_words = []
    for word in file_without_duplicates:
        if len(word)<4:
            short_words.append(word)
    
    #Se eliminan las stop words
    clean_file = []
    for count in file_without_duplicates:
        if count not in short_words:
            clean_file.append(count)
            
    #Se crea un nuevos archivos de texto para cada file procesado            
    with open(F'datos procesados/{namefile.split("/")[1]}procesado.txt', 'w', encoding="utf8" ) as f:
         f.write(' '.join(clean_file))
    
    return clean_file



files_list = os.listdir("raw_texts/")

for file in files_list:
    Data = CleanData('raw_texts/'+ file)
    dic_files[file]= Data
    resume_file = resume_file + Data
    final_resume_file = list(OrderedDict.fromkeys(resume_file))#Se une cada archivo procedado en una lista
    
    
with open('final_resume_file.txt', 'w', encoding="utf8" ) as f:
         f.write(' '.join(final_resume_file)) #Se une cada archivo procedado en un solo .txt