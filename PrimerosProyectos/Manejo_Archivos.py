from io import open


#Creacion y ingreso de datos
#archivo_texto=open("archivo.txt","w")
#frase="Estupendo día para estudiar Python \n el miércoles"
#archivo_texto.write(frase) ---escritura en el archivo
#archivo_texto.close() ---cierre de archivo

#archivo_texto=open("archivo.txt","r")
#texto=archivo_texto.read() #---lentura del archivo
#archivo_texto.close()
#print(texto) 

#archivo_texto=open("archivo.txt","r")
#linea_texto=archivo_texto.readline() # convierte el archivo en una lista
#archivo_texto.close()
#for i in linea_texto:
#    print(i)

#archivo_texto=open("archivo.txt","a")# extension o agregar 
#archivo_texto.write("\n Siempre es una buena ocacion para estudiar Python")  


archivo_texto=open("archivo.txt","r")

archivo_texto.seek(len(archivo_texto.read())/2)
#archivo_texto.seek(11)

print(archivo_texto.read()) 

