import re

class Tree():
    datos=[]
    def __init__(self, value):
        self.value = value
        self.izq= None
        self.dere=None

    def addLeft(self,padre,dato):
        if self.value!=padre:
            if self.izq!=None:
               self.izq.addLeft(padre,dato)
            if self.dere!=None:
               self.dere.addLeft(padre,dato)
            else:
               self.izq=Tree(dato)

    def addRight(self,padre,dato):
        if self.value!=padre:
            if self.izq!=None:
               self.izq.addRight(padre,dato)
            if self.dere!=None:
               self.dere.addRight(padre,dato)
            else:
               self.dere=Tree(dato)
 
    def searchNode(self,dato):
        if self.value!=dato:
            if self.izq!=None:
               return self.izq.searchNode(dato)
            if self.dere!=None:
               return self.dere.searchNode(dato)
            else:
               return self.value

    def imprimirArbolIzquierda(self):
        if self.value!= None:
            print (self.value)
            if self.izq!=None:
               self.izq.imprimirArbolIzquierda()
            if self.dere!=None:
               self.dere.imprimmirArbolIzquierda()

    def imprimirArbolDerecha(self):
        if self.value!=None:
            print (self.value)
            if self.dere!=None: 
               self.dere.imprimirArbolDerecha()
            if self.izq!=None:
               self.izq.imprimirArbolDerecha()



 
def main():
    archi=open('ejemplo.xml','r')
    linea=archi.readline()
    contador=0
    while linea!="":
           linea=archi.readline()
           linea=re.sub('[/<>=]', ' ', linea)
           lineajunta= linea
           atributos = linea.split('"')
           arbol=[]
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
                   arbol= arbol+listaDevice
           elif len(atributos)==3:
                     listaGroup=[]
                     for i in range(3):
                                 if i==1:
                                    id_group=atributos[i]
                                    listaGroup.append(id_group)
                     arbol= arbol+listaGroup
           elif len(atributos)==5:
                     listaCapability=[]
                     for i in range(5):
                                 if i==1:
                                    name=atributos[i]
                                    listaCapability.append(name)
                                 if i==3:
                                    value=atributos[i]
                                    listaCapability.append(value)
                     arbol= arbol+listaCapability
                     
    arbol=Tree(listaDevice)
    arbol.addLeft(listaDevice,listaGroup)
    arbol.addLeft(listaGroup,listaCapability)
    arbol.imprimirArbolIzquierda()
    

           
                                    

if __name__ == '__main__':
    main()
