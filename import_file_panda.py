import pandas as pd
import os

from collections import defaultdict # import defauldict

def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.','-', ',','*']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewLines(text):
    text=text.replace('\n', ' ')
    return text

def removeShortWords(text):
    return ' '.join([word for word in text.split() if len(word)>3])

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word)<4])

def splitByParagraphMark(text): # split log items by paragraph mark \n
    text= text.split('\n')

processingFunction = [lowercase]

#for func in processingFunction:
#    text = func(text)
#print(text)



# Read a CSV file into a DataFrame
#df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt',header=None,names=['date','time','none','pid','exe description', 'none2'])
df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt')
#Sintaxis : data=pandas.read_csv('filename.txt', sep=' ', header=None, names=[“Columna1”, “Columna2”])
#Parámetros:
#filename.txt: Como su nombre lo sugiere, es el nombre del archivo de texto del que queremos leer los datos.
#sep : Es un campo separador. En el archivo de texto, utilizamos el carácter de espacio (' ') como separador.
#header: este es un campo opcional. De manera predeterminada, tomará la primera línea del archivo de texto como encabezado. Si usamos header=None, creará el encabezado.
#nombres: Podemos asignar nombres de columnas al importar el archivo de texto utilizando el argumento de nombres.
# https://www.geeksforgeeks.org/how-to-read-text-files-with-pandas/
#df = pd.read_csv('example.csv')

#rows = int(df.shape[0])
#line = int(df.loc)
lines = 0
list = []
# print(df.columns[0])
# print(df.columns[1])
# print(df.columns[2])
# print(df.columns[3])
# print(df.columns[4])
while lines < df.shape[0]: # while line is lower than total number o lines of df
    #print(df.loc[lines])
    if df.loc[lines].empty == False: # Panda df serie is not empty
        text = df.loc[lines]
        text = text.to_string()
        list.append(text) # append each line (serie) of panda df to list
        #list.append(df.loc[lines]) # append each line (serie) of panda df to list
        lines = lines + 1
    else:
        pass
#print ((list[1]).split())



Log_lines = {
    'Info' : [''],
    'Perf' : [''],
    'PerfSproc' : [''],
    'Notice' : [''],
    'Warning' : [''],
    'Error' : [''],
    'Operation' : [''],
    'Other' : ['']
}
        
count = 0
count_perf = 0
count_PerfSproc = 0
count_info = 0
count_other = 0
count_notice = 0 
count_warning = 0
count_error = 0
count_operation = 0

for i in list:
    #print (i)
    text = i
    #text = i.to_string() # convert panda series to string --> https://sparkbyexamples.com/pandas/convert-pandas-series-to-string/#:~:text=Use%20the%20astype%20method%20in,Series%20into%20its%20string%20representation.
    #print (type(text))
# for loop that will get Log_lines items, iterate, appending to a dictionary where the key will be the type of log
    #print (text)
    if 'Perf: ' in text:
        Log_lines['Perf'].append(text)
        #print(text)
    elif 'PerfSproc: ' in text:
        Log_lines['PerfSproc'].append(text)
    elif 'Info:' in text:
        Log_lines['Info'].append(text)
        #print(text)
    elif 'Notice:' in text:
        Log_lines['Notice'].append(text)
    elif 'Warning:' in text:
        Log_lines['Warning'].append(text)
    elif 'Error:' in text:
        Log_lines['Error'].append(text)
    elif 'Operation:' in text:
        Log_lines['Operation'].append(text)
    else:
        Log_lines['Other'].append(text)
        #print(text)


    #for func in processingFunction:
    #    text = func(text)
        #print(text)
    
    count = count + 1
print (f'{count} registers processed!')

#print ('Log_lines keys')
#print(Log_lines.keys())
#print('Log_lines values')
#print(Log_lines.values())
print ('')
print ('---------------------------------------------------')
print ('')


#print(df.loc[1]) # --> https://realpython.com/pandas-dataframe/
#print (df.ndim)
#print (df.shape)
#shape = df.shape
#print (shape[0])
#print (df.size)


#print(Log_lines.items())
#print ('Log_lines keys')
#print(Log_lines.keys())
#print('Log_lines values')
#print(Log_lines.values())
print ('')
print ('---------------------------------------------------')
print ('')

print ('Len log lines')
print ('')
print(len(Log_lines))
print ('')
print ('---------------------------------------------------')
print ('')

# print ('Log lines: PerfSproc')
# print ('')
# print(Log_lines['PerfSproc'])
# print(Log_lines.get('PerfSproc'))
# print ('')
# print ('---------------------------------------------------')
# print ('')

print ('Log lines: Info')
print ('')
print(Log_lines['Info'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Notice')
print ('')
print(Log_lines['Notice'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Warning')
print ('')
print(Log_lines['Warning'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Error')
print ('')
print(Log_lines['Error'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Operation')
print ('')
print(Log_lines['Operation'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Perf')
print ('')
print(Log_lines['Perf'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Other')
print ('')
print(Log_lines['Other'])
print ('')
print ('---------------------------------------------------')
print ('')
