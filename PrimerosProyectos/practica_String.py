edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numérico")
    edad=input("Introduce la edad: ")

if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes pasar")


mailUsuario=input("Introduce tu correo electronico: ")

arroba=mailUsuario.count('@')
contador=0

while(arroba!=1 or mailUsuario.rfind('@') == (len(mailUsuario)-1)or mailUsuario.find('@')==0):
    print("Correo incorrecto, ejemplo @ mail . com")

for i in mailUsuario:
    if(i=='.'):
        contador+=1
    if contador>=1:
        print('Email es correcto')
    else: 
        print("Correo incorrecto ., ejemplo @ mail . com")
        mailUsuario=input("Introduce tu correo electronico: ")  



