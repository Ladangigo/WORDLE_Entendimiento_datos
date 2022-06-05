import random
import os

Archivos = []
MuestreoDatos = [ ]

lista_de_archivos = os.listdir("raw_texts/")

for archivo in lista_de_archivos:
    with open('raw_texts/' + archivo, 'r', encoding='utf8') as archivo_total:
        archivo_original = archivo_total.read()
        Archivos.append(archivo_original)
        listArchivo = archivo_original.split(' ')
        Muestra = int(len(listArchivo)/10) #Se hace un muestreo del 10% de los datos de cada archivo
        MuestreoDato = random.sample(listArchivo, Muestra)
        MuestreoDatos.append(MuestreoDato)
        
print(MuestreoDatos)