#modulos importados
import scrdr
import json

#nodo raiz
root = scrdr()
nombre = input("Root: ")

#input condiciones



#

while(input() != ":q"):







def clasificacion(node, atr):
    




def indexacion(node, nom, atr):
    cond = node.get_cond()
    
    if(cond.issubset(atr)):
        atr = atr.difference(cond)
    
    else: 
        new_node = node.get_else()
        if new_node != None:  #nodo tiene parte else
            indexacion(new_node,nom,atr)
        
        else:  #nodo no tiene parte else
            
            





