#!/usr/share/env python3
import re

'''
Proyecto de Lenguajes de Programacion
Parseo de un archivo xml e implementacion de queries
Integrantes: Dennise Pintado
             Janina Costa
             Jonathan Mendieta
'''

def main():
	testList = crearArbol()
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
				print ("Invalid option")
		except ValueError:
			print ("ERROR: Not a number")
			raw_input("\nPress Any Key to Continue")
	
def menuGraphics():
	print ("                  (    (     (           )    *     (      ")
	print (" (  (             )\ ) )\ )  )\ )     ( /(  (  `    )\ )   ")
	print (" )\))(   '    (  (()/((()/( (()/(     )\()) )\))(  (()/(   ")
	print ("((_)()\ )     )\  /(_))/(_)) /(_))   ((_)\ ((_)()\  /(_))  ")
	print ("_(())\_)() _ ((_)(_)) (_))_|(_))     __((_)(_()((_)(_))    ")
	print ("\ \((_)/ /| | | || _ \| |_  | |      \ \/ /|  \/  || |     ")
	print (" ( \/\/ / | |_| ||   /| __| | |__  _  >  < | |\/| || |__   ")
	print ("  \_/(_/   \___/ |_|_\|_|   |____|(_)/_/\_\|_|  |_||____|  ")
	print ("     )\ )                                                  ")
	print ("    (()/( (                (         (          (  (       ")
	print ("     /(_)))(    (    (    ))\ (   (  )\   (     )\))(      ")
	print ("    (_)) (()\   )\   )\  /((_))\  )\((_)  )\ ) ((_))\      ")
	print ("    | _ \ ((_) ((_) ((_)(_)) ((_)((_)(_) _(_/(  (()(_)     ")
	print ("    |  _/| '_|/ _ \/ _| / -_)(_-<(_-<| || ' \))/ _` |      ")
	print ("    |_|  |_|  \___/\__| \___|/__//__/|_||_||_| \__, |      ")
	print ("                                               |___/       ")
	print ("\nMenu:\n")
	print ("1.Search by ID")
	print ("2.Search by User_Agent")
	print ("3.Search by Fallback")
	print ("4.Search by Capabilities")
	print ("5.About")
	print ("6.Exit\n")

def crearArbol():
	arbol = []
	device = []
	capabilities = []
	archivo=open('wurfl-2.3.xml','r')
	linea=archivo.readline()
	while "<devices>" not in linea:
		linea=archivo.readline()
	linea = archivo.readline()
	linea=re.sub('[/<>=]"', '', linea)
	while "devices" not in linea:
		if "device" in linea:
			if device != []:
				arbol.append(device)
				device = []
			if "id" in linea and "user_agent" in linea and "fall_back" in linea:
				linea = linea.split("id")
				linea =  ','.join(linea)
				linea = linea.split("user_agent")
				linea =  ','.join(linea)
				linea = linea.split("fall_back")
				linea =  ','.join(linea)
				linea = linea.split('"')
				linea = ','.join(linea)
				linea = linea.split(',')
				device.append(linea[1])
				device.append(linea[3])
				device.append(linea[5])
			linea = archivo.readline()
			linea=re.sub('[/<>=]"', '', linea)
		elif "group" in linea and "id" in linea:
			
			linea = linea.split("id")
			linea =  ','.join(linea)
			linea = linea.split('"')
			linea = ','.join(linea)
			linea = linea.split(',')
			capabilities.append(linea[1])
			linea = archivo.readline()
			linea=re.sub('[/<>=]"', '', linea)
			if "capability" in linea:
				while "capability" in linea:
					linea = linea.split("capability name")
					linea =  ','.join(linea)
					linea = linea.split("value")
					linea =  ','.join(linea)
					linea = linea.split('"')
					linea = ','.join(linea)
					linea = linea.split(',')
					capabilities.append([linea[1],linea[3]])
					linea = archivo.readline()
					linea=re.sub('[/<>=]"', '', linea)
			device.append(capabilities)
			linea = archivo.readline()
			linea=re.sub('[/<>=]"', '', linea)
	
	return arbol
	

##Funciones para Menu Principal
#---------------------------------------------------------------
#Menu: Buscar por ID
def menuBuscarxID(deviceList):
	IDs = []
	devicesFound = []
	Verifier = ""
	print ("\nInput the ID String to search (can contain substrings), press 'Enter' to enter a new value and type 'OK' to finish:\n")
	while Verifier != "OK":
		Verifier = raw_input('')
		if Verifier != "OK":
			IDs.append(Verifier)
	devicesFound = searchDeviceByID(deviceList,IDs)
	print ("\nDEVICES FOUND:\n")
	for i in range (0,len(devicesFound)):
		print (devicesFound[i][0])
	print ("\nNUMBER OF DEVICE FOUND: "+str(len(devicesFound)))
	
#Menu: Buscar por User_Agent
def menuBuscarxUser(deviceList):
	devicesFound = []
	User_agent = raw_input("\nInput the User_Agent to search:\n")
	devicesFound = searchDevicebyUserAgent(deviceList,User_agent)
	print ("\nDEVICES FOUND:\n")
	for i in range (0,len(devicesFound)):
		print (devicesFound[i][0])
	print ("\nNUMBER OF DEVICE FOUND: "+str(len(devicesFound)))

#Menu: Buscar por Fallback
def menuBuscarxFallback(deviceList):
	devicesFound = []
	Fallback = raw_input("\nInput the Fallback to search:\n")
	devicesFound = searchDevicebyFallback(deviceList, Fallback)
	print ("\nDEVICES FOUND:\n")
	for i in range (0,len(devicesFound)):
		print (devicesFound[i][0])
	print ("\nNUMBER OF DEVICE FOUND: "+str(len(devicesFound)))	

#Menu: Buscar por Capability
def menuBuscarxCapability(deviceList):
	capabilities = []
	devicesFound = []
	verifier = ""
	print ("\nInput the capabilities to search, as follow: 'capability_name value', press 'Enter' to enter a new value and type 'OK' to finish:\n")
	while verifier != "OK":
		verifier = raw_input('')
		if verifier != "OK":
			capabilities.append(verifier.split(' '))
	devicesFound = searchDevicebyCapability(deviceList,capabilities)
	print ("\nDEVICES FOUND:\n")
	for i in range (0,len(devicesFound)):
		print (devicesFound[i][0])
	print ("\nNUMBER OF DEVICE FOUND: "+str(len(devicesFound)))

#Menu: Acerca de
def menuAcercade(deviceList):
	print ("\nProject of Programming Languages WURFL.XML Processing\n\nCollaborators:\n\n-Jonathan Mendieta\n-Janina Costa\n-Denisse Pintado")
			
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
