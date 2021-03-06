# Se importan las librerías
import re
from collections import OrderedDict
import nltk
from nltk.corpus import stopwords
import os
nltk.download('stopwords')
stop_words = stopwords.words('spanish')


dic_files = {}
final_resume_file = []
resume_file = []

def clean_data(namefile):
    # namefile ---> ruta del archivo al cual se realizá el proceso de limpieza
    # CleanData: Hace un proceso de limpieza a cada uno de los archivos que estan en la carpeta "raw_texts/" 
    # que consisite en los siguientes pasos:

    # 1.Elimina todos los carácteres o síbolos
    # 2. Se eliminan palabras con mas de dos mayúsculas
    # 3. Se cambian vocales con tíldes por sus homólogos sin estas
    # 4. Se eliminan los dígitos númericos y otros acentos 
    # 5. Se eliminan palabras duplicadas 
    # 6. Se eliminan las stop worsd
    # 7. Se eliminan palabras con una longitud menor a 3
    # Una vez realizado todo este proceso de limpieza de datos, se crea una carpeta la cual 
    # contendrá cada uno de los archivos aquí procesados
    # La función retorna una lista que contiene las palabras válidas para ser parte del 
    # banco de palabras de cada .txt

    
    with open(namefile, 'r',encoding="utf8") as raw_file:
        original_file = raw_file.read()
        
    
    # Eliminar símbolos
    symbols = ['¿','?','~','`','!','¡','@','#','$','%','^','*','(',')','_','-','+','=','{','}','[',']','\\',':',';','<','>','/', '.', ',','&','\r','\t', '|', '“', '"', '–', '”', '©', '-', '—','…', ';', '‘','’',"'",'\xa0']
    for char in symbols:
        original_file = original_file.replace(char,' ')

    # Elimino las palabras que contengan mas de dos mayúsculas
    delete_uppcase1 = re.sub(r'([A-Z]\w+[A-Z]\w+)',"", original_file)
    delete_uppcase2 = re.sub(r'[A-Z]{2,}','',delete_uppcase1)
        
    
    # cambia todo a minúsculas 
    file_lowercase = delete_uppcase2.lower()
   
    # cambio acentos
    vowels = ((r'á','a'),(r'é','e'),(r'í','i'),(r'ó','o'),(r'ú','u'))
    for i in vowels:
        file_lowercase = re.sub(i[0],i[1], file_lowercase)


    # Solo letras
    file_without_numbers = [ ]
    file_without_numbers = re.findall(r'[aA-zZÑñ]+', file_lowercase)
      
    # Eliminar duplicados
    file_without_duplicates = [ ]
    file_without_duplicates = list(OrderedDict.fromkeys(file_without_numbers))   
    
    
    # Elimino stopwprds
    file_without_stopwords = []
    for item in file_without_duplicates:
      if not item in stop_words:
        file_without_stopwords.append(item)

    # se eliminan las palabraas menores a 4 letras
    clean_file=file_without_stopwords.copy()
    word= None
    for word in file_without_stopwords:
      if len(word)<4:
        clean_file.remove(word)    
    

            
    # Se crea un nuevos archivos de texto para cada file procesado            
    with open(F'datos procesados/{namefile.split("/")[1]}procesado.txt', 'w', encoding="utf8" ) as f:
         f.write(' '.join(clean_file))
    
    return clean_file



files_list = os.listdir("raw_texts/")

for file in files_list:
    Data = clean_data('raw_texts/'+ file)
    dic_files[file]= Data
    resume_file = resume_file + Data
    final_resume_file = list(OrderedDict.fromkeys(resume_file))# Se une cada archivo procedado en una lista
    
    
with open('final_resume_file.txt', 'w', encoding="utf8" ) as f:
         f.write(' '.join(final_resume_file)) # Se une cada archivo procedado en un solo .txt