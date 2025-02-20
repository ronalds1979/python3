import pandas as pd
import os
# Read a CSV file into a DataFrame
df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt',header=None,names=['date','time','none','pid','exe description', 'none2'])
#Sintaxis : data=pandas.read_csv('filename.txt', sep=' ', header=None, names=[“Columna1”, “Columna2”])
#Parámetros:
#filename.txt: Como su nombre lo sugiere, es el nombre del archivo de texto del que queremos leer los datos.
#sep : Es un campo separador. En el archivo de texto, utilizamos el carácter de espacio (' ') como separador.
#header: este es un campo opcional. De manera predeterminada, tomará la primera línea del archivo de texto como encabezado. Si usamos header=None, creará el encabezado.
#nombres: Podemos asignar nombres de columnas al importar el archivo de texto utilizando el argumento de nombres.
# https://www.geeksforgeeks.org/how-to-read-text-files-with-pandas/
#df = pd.read_csv('example.csv')
#print(df)
for line in df:
    print (line)
    #print(line.split())
    



