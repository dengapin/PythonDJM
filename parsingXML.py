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
	testList = [["olakase","2","3",["GG",["como","false"],["comoxA","false"],["waffle","false"],["sardina","true"]]],["olakase2","2","3",["XD",["waffle","true"],["como","false"],["sardina","true"]]]]
	option = 0
	menuOptions = {1:menuBuscarxID,2:menuBuscarxUser,3:menuBuscarxFallback,4:menuBuscarxCapability,5:menuAcercade}
	while option is not 6:
		menuGraphics()
		try:
			option=int(raw_input('Select option:'))
			if option < 6 and option >0:
				menuOptions[option](testList)
				raw_input("\nPress Any Key to Continue")
			elif option is not 6:
				print "Invalid option"
		except ValueError:
			print "ERROR: Not a number"
			raw_input("\nPress Any Key to Continue")
	#print formaArbol()

def menuGraphics():
	print "                  (    (     (           )    *     (      "
	print " (  (             )\ ) )\ )  )\ )     ( /(  (  `    )\ )   "
	print " )\))(   '    (  (()/((()/( (()/(     )\()) )\))(  (()/(   "
	print "((_)()\ )     )\  /(_))/(_)) /(_))   ((_)\ ((_)()\  /(_))  "
	print "_(())\_)() _ ((_)(_)) (_))_|(_))     __((_)(_()((_)(_))    "
	print "\ \((_)/ /| | | || _ \| |_  | |      \ \/ /|  \/  || |     "
	print " ( \/\/ / | |_| ||   /| __| | |__  _  >  < | |\/| || |__   "
	print "  \_/(_/   \___/ |_|_\|_|   |____|(_)/_/\_\|_|  |_||____|  "
	print "     )\ )                                                  "
	print "    (()/( (                (         (          (  (       "
	print "     /(_)))(    (    (    ))\ (   (  )\   (     )\))(      "
	print "    (_)) (()\   )\   )\  /((_))\  )\((_)  )\ ) ((_))\      "
	print "    | _ \ ((_) ((_) ((_)(_)) ((_)((_)(_) _(_/(  (()(_)     "
	print "    |  _/| '_|/ _ \/ _| / -_)(_-<(_-<| || ' \))/ _` |      "
	print "    |_|  |_|  \___/\__| \___|/__//__/|_||_||_| \__, |      "
	print "                                               |___/       "
	print "\nMenu:\n"
	print "1.Search by ID"
	print "2.Search by User_Agent"
	print "3.Search by Fallback"
	print "4.Search by Capabilities"
	print "5.About"
	print "6.Exit\n"

def formaArbol():
    archi=open('ejemplo.xml','r')
    linea=archi.readline()
    cont=0
    #El archivo se lee hasta que ya no encuentre mas lineas en el xml
    while linea!="":
           linea=archi.readline()
           #Se reemplazan estos caracteres en espacio en blanco
           linea=re.sub('[/<>=]', ' ', linea)
           lineajunta= linea
           #Se separan por comillas la lista que correspondera a los atributos
           atributos = linea.split('"')
           arbolito=[]
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
    #return arbolito        
    #print searchDeviceByID(arbolito,["sony","sub"])
    #print searchDevicebyFallback(arbolito,"sonyericsson_p990i_ver1")
    #print searchDevicebyCapability([["1","2","3",["GG",["como","false"],["comoxA","false"],["waffle","false"],["sardina","true"]]],["1","2","3",["XD",["waffle","true"],["como","false"],["sardina","true"]]]],[["como","false"],["sardina","true"]])

##Funciones para Menu Principal
#---------------------------------------------------------------
#Menu: Buscar por ID
def menuBuscarxID(deviceList):
	IDs = []
	Verifier = ""
	print "Input the ID String to search (can contain substrings), press 'Enter' to enter a new value and type 'OK' to finish:"
	while Verifier != "OK":
		Verifier = raw_input('')
		if Verifier != "OK":
			IDs.append(Verifier)
	print searchDeviceByID(deviceList,IDs)
	
#Menu: Buscar por User_Agent
def menuBuscarxUser(deviceList):
	print searchDevicebyUserAgent(deviceList,raw_input("Input the User_Agent to search:\n"))

#Menu: Buscar por Fallback
def menuBuscarxFallback(deviceList):
	print searchDevicebyFallback(deviceList,raw_input("Input the Fallback to search:\n"))

#Menu: Buscar por Capability
def menuBuscarxCapability(deviceList):
	capabilities = []
	verifier = ""
	print "Input the capabilities to search, as follow: 'capability_name value', press 'Enter' to enter a new value and type 'OK' to finish:"
	while verifier != "OK":
		verifier = raw_input('')
		if verifier != "OK":
			capabilities.append(verifier.split(' '))
	print searchDevicebyCapability(deviceList,capabilities)

#Menu: Acerca de
def menuAcercade(deviceList):
	print "\nProject of Programming Languages WURFL.XML Processing\n\nCollaborators:\n\n-Jonathan Mendieta\n-Janina Costa\n-Denisse Pintado"
#---------------------------------------------------------------

##Funciones para buscar Query por ID
#---------------------------------------------------------------
#Funcion para analizar el query de encontrar substrings en el ID
def searchDeviceByID(deviceList,idSubstringList):
	devicesFoundList = []
	for device in deviceList:
		if stringContainsStrings(device[0],idSubstringList):
			devicesFoundList.append(device)
	return devicesFoundList

#Funcion que verifica si existen substrings en el string dado, devuelve Verdadero si los substring son encontrados y Falso si no
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

#Funcion para buscar Query por User_Agent
def searchDevicebyUserAgent(deviceList,user_agent):
	deviceFoundList = []
	for device in deviceList:
		if user_agent in device[1]:
			deviceFoundList.append(device)
	return deviceFoundList

#Funcion para buscar Query por Fallback
def searchDevicebyFallback(deviceList,fallback):
	deviceFoundList = []
	for device in deviceList:
		if fallback in device[2]:
			deviceFoundList.append(device)
	return deviceFoundList

##Funcion para buscar Query por capability
#---------------------------------------------------------------	
#Funcion que busca cada device en el arbol y verifica sus capabilities con el valor booleano dado
def searchDevicebyCapability(deviceList,capabilityList):
	deviceFoundList = []
	for device in deviceList:
		if capabilityContained(device,capabilityList):
			deviceFoundList.append(device)
	return deviceFoundList

#Funcion para verificar si existe un device con tales capabilities, retorna Verdadero si TODOS los capabilities son encontrados, y Falso si por lo menos uno no	es
def capabilityContained(device,capabilityList):
	countTester = 0
	for capability in capabilityList:
		flag = 0
		for i in range(3,len(device)):
			for j in range(1,len(device[i])):
				if (device[i][j][0]==capability[0] and device[i][j][1]==capability[1]):
					countTester+=1
					if countTester==len(capabilityList):
						return True
					flag+=1
					break
			if flag == 1:
				break
		if flag == 0:
			return False
#---------------------------------------------------------------	

if __name__ == '__main__':
    main()
