import random
import os

Archivos = []
MuestreoDatos = [ ]

lista_de_archivos = os.listdir("raw_texts/")

#Muestreo de datos dados por el cliente
for archivo in lista_de_archivos:
    with open('raw_texts/' + archivo, 'r', encoding='utf8') as archivo_total:
        archivo_original = archivo_total.read()
        Archivos.append(archivo_original)
        listArchivo = archivo_original.split(' ')
        Muestra = int(len(listArchivo)/10) #Se hace un muestreo del 10% de los datos de cada archivo
        MuestreoDato = random.sample(listArchivo, Muestra)
        MuestreoDatos.append(MuestreoDato)
        
print(MuestreoDatos)

with open('uniondearchivos.txt', 'w', encoding='utf8') as f:
    f.write(''.join(Archivos)) #Se unen todos los archivos en uno solo

#Muestreo de datos ya una vez pasado por un proceso de limpieza
with open('/content/Data/final_resume_file.txt', 'r',encoding="utf8") as raw_file:
    archivo = raw_file.read()
    final_resume_file = archivo.split(' ')
    muestra = int(len(final_resume_file)/10)
    MuestreoDatosLimpios = random.sample(final_resume_file, muestra)

print(MuestreoDatosLimpios)
  