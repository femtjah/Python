import pickle

#lista_nombre= ["Pedro","Ana","María","Isabel"] Pasar lista a codificacion binaria 
#fichero_binario=open("lista_nombre","wb")
#pickle.dump(lista_nombre, fichero_binario)
#fichero_binario.close()
#del (fichero_binario)

fichero=open("lista_nombre", "rb") #Rescatar la lista del codigo binario. 
lista=pickle.load(fichero)
print(lista)

