
def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')

def leertxt():
        archi=open('datos.txt','r')
        for linea in archi.readlines(): 
             print (linea )
        archi.close() 

     
creartxt()
grabartxt()
leertxt()

