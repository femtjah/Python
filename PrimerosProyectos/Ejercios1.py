"""
1- definir una funcion max() que tome como argumento 
dos numeros y devuelva el mayor de ellos.
"""
def funcion_max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
print (funcion_max(9, 11))

"""
definir una funcion max_de_tres(), que tome tres números 
como argumentos y retorne el mayor
"""
def funcion_max_tres(n1,n2,n3):
    
    if n1>n2 and n1 > n3:
        return n1 
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

print (funcion_max_tres(7,3,6))

# Vocales
def is_vocal(carater):
    lista_vocales = ['a','e','i','o','u']
    if carater in lista_vocales:
        return True
    else:
        return False
print(is_vocal('b'))

# suma de lista
def sum(list):
    result = 0 
    for n in list:
        result = result + (n)
    print(result)
sum([1,5,-3])

# Multiplicacion de lista
def mult(list):
    result = list[0]
    i = 1
    while i in range(1, len(list)):
        result = result * list[i]
        i += 1
        print(result)
mult([2,2,2])

"""
Definir una funcion inversa() qued calcule la inversión de una cadena
"""
def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena= str()
    for n in range(longitud, 1):
        n = abs(n)
        nueva_cadena += cadena[n]
    print(nueva_cadena)
    return nueva_cadena
    
inversa('Fabio')

# funcion palabra palindromo

def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True
    else:
        print('Palabra no es un Palindromo')
print(es_palindromo('arenera'))

# super posicion
def superposicion(list1, list2):
    for elem in list1:
        for elem2 in list2:
            if elem == elem2:
                return True
    return False

    """
    for elem in list1:
        if elem in list2:
            return True
    return False
    """
resultado = superposicion([1,2,3],[3,4,5])
print('Superposicion: '+ str(resultado))

# N caracteres 
def geneara_n_caracteres(caracter, n):
    string = caracter
    for i in range(1,n):
        string += caracter
    print(string)
geneara_n_caracteres('adc',2)

# histograma
def procedimiento(lista):
    for n in lista:
        histograma = '*' * n
        print(f'{histograma} \n')

procedimiento([1,2,4,3,2,1])


# Categorizacion especial 
def categorizacion(list1):
    for i in list1:
        n = len(i)
        caracter=(i[0])
        print(caracter + str(n))
categorizacion(['Harry potter','The Hunger Games','Pride and Presudice','Gone with the Wind'])



