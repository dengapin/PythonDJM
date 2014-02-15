#!/usr/share/env python3
import re

'''
Proyecto de Lenguajes de Programacion
Parseo de un archivo xml e implementacion de queries
Integrantes: Dennise Pintado
             Janina Costa
             Jonathan Mendieta
'''

#Querie mostrar devices en los que el fall_back sea un string especifico
#              if len(atributos)==7:
#               listaDevice=[]
#               for i in range(7):
#                          if i==5:
#                             fall_back=atributos[i]
#                             if fall_back=="nokia_6681_ver1":
#                                listaDevice.append(fall_back)
#                                print(listaDevice)
 
def main():
    archi=open('test.xml','r')
    linea=archi.readline()
    cont=0
    arbolito=[]
    #El archivo se lee hasta que ya no encuentre mas lineas en el xml
    while linea!="":
           linea=archi.readline()
           #Se reemplazan estos caracteres en espacio en blanco
           linea=re.sub('[/<>=]', ' ', linea)
           lineajunta= linea
           #Se separan por comillas la lista que correspondera a los atributos
           atributos = linea.split('"')
           #Si la dimension de la lista es la indicada correspondera sin duda al grupo mencionado
           if len(atributos)==7:
               listaDevice=[]
               for i in range(7):
                          if i==1:
                             id_device=atributos[i]
                             listaDevice.append(id_device)
                          if i==3:
                             user_agent=atributos[i]
                             listaDevice.append(user_agent)
                          if i==5:
                             fall_back=atributos[i]
                             listaDevice.append(fall_back)
           elif len(atributos)==3:
               listaGroup=[]
               for i in range(3):
                                 if i==1:
                                    id_group=atributos[i]
                                    listaGroup.append(id_group)
           elif len(atributos)==5:
               listaCapability=[]
               for i in range(5):
                                 if i==1:
                                    name=atributos[i]
                                    listaCapability.append(name)
                                 if i==3:
                                    value=atributos[i]
                                    listaCapability.append(value)
               listaGroup.append(listaCapability)
               listaDevice.append(listaGroup)
           #El device terminara cuando encuentre el tag de cierre de Device
           if len(linea)==12:
               cont=cont+1
               print("*****-----------------------------Device"+" "+str(cont)+"-----------------------*******")
               print(listaDevice) 
               arbolito.append(listaDevice)
    print searchStringinID(arbolito,["sony","sub"])

##Funciones para buscar Query por ID
#---------------------------------------------------------------
#Funcion para analizar el query de encontrar substrings en el ID
def searchStringinID(deviceList,idSubstringList):
	devicesFoundList = []
	for device in deviceList:
		if stringContainsStrings(device[0],idSubstringList):
			devicesFoundList.append(device)
	return devicesFoundList

#Funcion que verifica si existen substrings en el string dado, devuelve Verdadero si los substring son encontrados y Falso si no lo son.
def stringContainsStrings(deviceID,stringList):
	boolTester = []
	for i in range (0,len(stringList)):
		if stringList[i] in deviceID:
			boolTester.append(True)
		else:
			boolTester.append(False)
	for j in range (0,len(boolTester)):
		if boolTester[j] == False:
			return False
	return True
#---------------------------------------------------------------	

if __name__ == '__main__':
    main()
