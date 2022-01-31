def divide():
    try:        
        op1=(float(input('Introduce el primer numero: ')))
        op2=(float(input('Introduce el segundo numero: ')))

        print('La división es: '+ str(op1/op2))
    except ValueError:
        print('El valor introducido es erróneo')
    except ZeroDivisionError:
        print('No se puede dividir en  0')    
    print('Cálculo finalizado')
