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
        linea = re.sub('[/<>"=]', '', linea)
        atributos = linea.split(' ')
        tag=[]
        if 'device' in linea:
               if len(linea)>6:
                      for i in range(4):
                             if i==1:
                                    a=atributos[i].replace("id_device",'')
                                    tag.append(a)
                             if i==2:
                                    b=atributos[i].replace("user_agent",'')
                                    bb= b.replace(" ",'_')
                                    tag.append(bb)
                             if i==3:
                                    c=atributos[i].replace("fall_back",'')
                                    tag.append(c)
                      print(tag)
               
         
leer()
