import re

def leer():
       archi=open('ejemplo.xml','r')
       linea=archi.readline()
       contador=0
       while linea!="":
              linea=archi.readline()
              contador +=1
              parsear(contador,linea.strip())

def parsear(contador,linea):
        linea = re.sub('[/<>=]', ' ', linea)
        lineajunta= linea
        listaAtributos=[]
        atributos = linea.split('"')
        if len(atributos)==7:
               for i in range(7):
                      if i==1:
                         id_device=atributos[i]
                         listaAtributos.append(id_device)
                      if i==3:
                         user_agent=atributos[i]
                         listaAtributos.append(user_agent)
                      if i==5:
                         fall_back=atributos[i]
                         listaAtributos.append(fall_back)
               print(listaAtributos)   
        elif len(atributos)==5:
                 for i in range(5):
                             if i==1:
                                name=atributos[i]
                                listaAtributos.append(name)
                             if i==3:
                                value=atributos[i]
                                listaAtributos.append(value)
                 print(listaAtributos)
        elif len(atributos)==3:
                 for i in range(3):
                             if i==1:
                                id_group=atributos[i]
                                listaAtributos.append(id_group)
                 print(listaAtributos)             
leer()
