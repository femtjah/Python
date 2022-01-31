lst = [1,2]
for v in range(2):
    lst.insert(-1, lst[v])
print(lst)    


def func(a, b):
    return b ** a
print (func(2, 2)) 

z = 0 
y = 10
x = y < z and z > y or y >z and z < y
print (x)

list = [x * x for x in range(5)]
def fun (lst):
    del lst[lst[2]]
    return lst
print(fun(list))

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

def fun(x):
    if x % 2 == 0:
        return 1 
    else:
        return 2
print (fun(fun(2)))     

nums = [1,2,3]
vals = nums
del vals[:]

print (nums)
print(vals)


#x = x % y
#x = x % y
#y = y % x
#print(y)

#y =input()
#x=input()
#print(x + y)

print('a', 'b', 'c', sep='sep')

x = 1 // 5 + 1 / 5

print(x)
#x = int(input())
#y = int(input())
print(y **(1/x))

def fun (inp=2, out=3):
    return inp * out

print(fun(out=2))    

dct = {'uno':'dos','tres':'uno','dos':'tres'}
v = dct['tres']

for k in range(len(dct)):
    v = dct[v]

print(v)    

lst = [i for i in range(-1,-2)]

print(lst)

def fun(x, y):
    if x == y :
        return x 
    else:
        return fun(x, y-1)
print(fun(0,3))       

#i= 0

#while i < i + 2:
 #   i +=1 
  #  print('*')
#else:
#    print('*')    

tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

#dd = {'1':'0', '0':'1'}
#for x in dd.vals():
#    print(x, end=)

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)
for x in dct.keys():
    print(dct[x][1],end='')

lst = [[x for x in range(3)]for y in range(3)]    
for r in range (3):
    for c in range(3):
        if lst[r][c]% 2 != 0: 
            print('#')

#Listas
miLista = ['Maria', 'Pepe', 'Marta','Antonio']

miLista.append('Sandra')#agrega elemento al final .append
miLista.insert(2,'Marco')#agrega elemento en el Indice (3,'nombre') .insert
miLista.extend(['Fidel','Ana','Lucia'])#agregar mas elementos a la lista
miLista.remove('Ana')#eliminar elemento
miLista.pop()#elimina Ultimo elemento

print(miLista[:])#Toda la lista
print(miLista[0:3])#Porcion de Lista [:2] [1:4] [2:]
print(miLista.index('Fidel'))#en que posicion esta Ana en la lista
print('Pepe' in miLista)# esta o no el elemento? in

miLista2 = ['Fabio', 'Mario']
miLista3 = miLista + miLista2 
print(miLista3[:])

#Tuplas:     listas inmutables, no se pueden modificar y con ()
miTupla=('Juan',13,1,1995,13,13)
print(miTupla[:])
print(miTupla[1])
print('Juan' in miTupla) #esta el elemento en la tupla? 
print(miTupla.count(13))#cuantas veces esta el elemento en la Tupla
print(len(miTupla))#cuantos elementos tiene la Tupla

#Diccionarios:   
miDiccionario= {'Alemania':'Berlin','Francia':'Paris','Reino Unido':'Londres','España':'Madrid'}
miDiccionario['Italia']='Lisboa' #Agregar elemento al Dieccionario
print(miDiccionario['Alemania'])
print(miDiccionario) 
miDiccionario['Italia']='Roma' #modificar elemento del Diccionario
print(miDiccionario) 
del miDiccionario['Reino Unido'] # eliminar elemento del Diccionario
print(miDiccionario)
print(miDiccionario.keys())# Claves del diccionario
print(miDiccionario.values())# Valores del diccionario
print(len(miDiccionario)) # cuantos elementos tiene el dieccionario

#Condicional If
print('programa de evaluación de nota de alumnos')
nota_alumno=int (input('Introduce la nota del alumno: '))
def evalucion(nota):
    valoracion = 'aprobado'
    if nota<5:
        valoracion='suspenso'
    return valoracion
print(evalucion(nota_alumno))    

#If else elif
print('Verificacion de acceso')
edad_Usuario=int(input('Introduce tu edad, por favor: '))
if edad_Usuario<18:
    print('No puedes pasar')
elif edad_Usuario>100:
    print('Edad incorrecta')    
else:
    print('Puedes pasar')
print('Programa a finalizado')
  

# Codigo Salarios

salario_presidente = int(input('Introduce salario presidente '))
print('Salario presidente: '+ str(salario_presidente))  
salario_director = int(input('Introduce salario director '))
print('Salario director: '+ str(salario_director))  
salario_jefe_area = int(input('Introduce salario jefe Área '))
print('Salario Jefe Área: '+ str(salario_jefe_area))  
salario_administrativo = int(input('Introduce salario Administratico '))
print('Salario Administrativo: '+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('Todo funciona correctamente ')
else:
    print('Algo falla en esta empresa')    


# Curso con Beca AND y OR
print('Programa de becas Año 2021')
distancia_escuela= int(input('Introduce la distancia a la escuala en Km '))
print(str(distancia_escuela)+'Km')
numero_hermanos= int(input('introduce el numero de hermanos en el centro '))
print(numero_hermanos)
salario_familiar=int(input('introduce salio anual bruto '))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print('Tiene derecho a beca')

else:
    print('No tienes derecho a beca')    


# Asignaturas Operador IN 

print('Asignaturas optativas Año 2021')
print('Asignaturas optavivas: Informatica grafica - Pruebas de spftware - Usabilidad y accesibilidad')
opcion=input('Escribe la asignatura escogida: ')
asignatura = opcion.lower()
if asignatura in('informatica grafica' , 'pruebas de software' , 'usabilidad y accesibilidad'):
    print('Asignatura elegida: ' + asignatura)
else:
    print('La asignatura escogida no está contemplada')


# Bucle For
# FOR variable IN Elemento a recorrer:
    #Codigo a Ejecutar 
for i in ['Primavera', 'Verano','Otoño','Invierno']:
    print('Hola')

#validacion de un Email

miEmail= input('Introduce tu direccíon de email: ')
for i in miEmail:
    if i=='@':
        arroba= True
        break
else: 
    arroba=False
    print('El correo necesita un @')
 
if arroba == True:
    contador= 0
    for i in miEmail:
        if(i=='.'):
            contador+=1
    if contador==1 or contador ==2:
        print('Email es correcto')
    else: 
        print('El email no es correcto')              

# f para ingresar el valor de la variable 
for i in range(5):
    print(f'Valor de la variable {i}')


# Bucle While
i=1
while i <= 10:
    print("ejecucion "+str(i))
    i=i+1
print('Termino la ejecución')    

edad=int(input('Introduce tu edad por favor: '))

while edad<5 or edad>100:
    print('Has introducido uns edad negativa. Vuelve a intentarlo')
    edad= int(input('Introduce tu edad por favor: '))
print('Gracias por colaborar. Puedes pasar')
print('edad del aspirante '+ str(edad))


# Raíz
import math
print('Programa de cálculo de raíz cuadrada')
numero= int(input('Introduce un numero por favor: '))

intetos=0
while numero<0:
    print('No se puede hallar la raíz de un número negrativo')
    if intentos==2:
        print('has consumido demasidos intentos. el programa ha finalizado')
        break;
    numero= int(input('Introduce un número por favor: '))
    if numero<0:
        intentos=intentos+2
if intentos<2:
    solucion=math.sqrt(numero)
    print('La raíz cuadrada de '+str(numero)+'es'+str(solucion))            

#Numeros mayores
numero1 =int(input('Ingresa un numero: '))
numero2 =int(input('ingresa un numero mayor que '+ str(numero1)+': '))
while numero2 > numero1:
    numero1 = numero2
    numero2= int(input('Escriba un numero mayor que '+ str(numero1)+': '))
print()
print(numero2, 'no es mayor que', str(numero1)) 


#Numeros Positivos
num = int(input('Ingresa un numero: '))
suma = 0
while num>0:
    suma =suma+num
    num = int(input('Ingresa otro número: '))

print('La suma de los números introducidos es: '+str(suma))    

#Generadores Yield
def generaPares(limite):
    num = 1
    
    while num<limite:
        yield num*2
        num+=1
devuelvePares=generaPares(10)    

#for i in devuelvePares:
    #print(i)         

print(next(devuelvePares))
print('Aqui prodria ir mas codigo...')
print(next(devuelvePares))
print('Aqui prodria ir mas codigo...')
print(next(devuelvePares))              

# Generador Yield From
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudadesDevueltas=devuelveCiudades('Madrid','Barcelona','Bilbao','Valencia')
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

#Excepciones 
 
 
