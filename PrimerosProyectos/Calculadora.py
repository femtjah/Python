#Excepciones
def div(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return'Operación errónea'   

def mul(num1, num2):
    return num1*num2

def res(num1, num2):
    return num1-num2

def sum(num1,num2):
    return num1+num2    

while True:
    try:
        op1= int(input('Introduce un primer número: '))
        op2= int(input('Introduce un segundo número: '))
        break
    except ValueError:
        print('Los valores introducidos no son correctos. Intentalo de nuevo')

operacion=(input('Introduce una operacion a realizar (suma, resta, multiplica, divide): '))

if operacion=='divide':
    print(div(op1,op2))
elif operacion=='multiplica':
    print(mul(op1,op2))
elif operacion=='resta':
    print(res(op1,op2))
elif operacion=='suma':
    print(sum(op1,op2))
else:
    print('Operacion no contemplada')

print('Operacion ejecutada. continuacion de ejecucion del programa')

