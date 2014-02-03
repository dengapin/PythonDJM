import re
 
def main():
    archi=open('ejemplo.xml','r')
    linea=archi.readline()
    cont=0
    while linea!="":
           linea=archi.readline()
           linea=re.sub('[/<>=]', ' ', linea)
           lineajunta= linea
           atributos = linea.split('"')
           arbolito=[]
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
               
           if len(linea)==12:
               cont=cont+1
               print("*****-----------------------------Device"+" "+str(cont)+"-----------------------*******")
               print(listaDevice) 
               

if __name__ == '__main__':
    main()
