#Se importan las librerías
import re
import unidecode 
from collections import OrderedDict
import nltk
from nltk.corpus import stopwords
import os
nltk.download('stopwords')
stop_words = stopwords.words('spanish')

dic_files = {}
final_resume_file = []
resume_file = []