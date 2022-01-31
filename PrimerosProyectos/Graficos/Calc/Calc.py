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