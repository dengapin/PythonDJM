import re

def leer():
       archi=open('ejemplo.xml','r')
       linea=archi.readline()
       contador=0
       while linea!="":
              linea=archi.readline()
              contador +=1
              tomar(contador,linea.strip())

def parsear(contador,linea):
        linea = re.sub('[<>/]', '', linea)
        print(str(contador)+str(linea))
        
        
     
leer()

