
historial = []


def get_sumando1():
    try:
        return float(input('Ingrese el primer sumando: '))
    except:
        print('No ingresó un número válido.')
        return get_sumando1()
    

def get_sumando2():
    try:
        return float(input('Ingrese el segundo sumando: '))
    except:
        print('No ingresó un número válido.')
        return get_sumando2()
    

def get_minuendo():
    try:
        return float(input('Ingrese el minuendo: '))
    except:
        print('No ingresó un número válido.')
        return get_minuendo()


def get_sustraendo():
    try:
        return float(input('Ingrese el sustraendo: '))
    except:
        print('No ingresó un número válido.')
        return get_sustraendo()


def get_factor1():
    try:
        return float(input('Ingrese el primer factor: '))
    except:
        print('No ingresó un número válido.')
        return get_factor1()


def get_factor2():
    try:
        return float(input('Ingrese el segundo factor: '))
    except:
        print('No ingresó un número válido.')
        return get_factor2()


def get_dividendo():
    try:
        return float(input('Ingrese el dividendo: '))
    except:
        print('No ingresó un número válido.')
        return get_dividendo()


def get_divisor():
    try:
        divisor = float(input('Ingrese el divisor: '))
        if divisor == 0:
            print('No se puede dividir por cero.\nIngrese un número válido.')
            return get_divisor()
        else:
            return divisor #float(input('Ingrese el divisor: '))
    except:
        print('No ingresó un número válido.')
        return get_divisor()


def sumar():
    number1 = get_sumando1() #float(input('Ingrese el primer sumando: '))
    number2 = get_sumando2() #float(input('Ingrese el segundo sumando: '))
    resultado = number1 + number2 #suma
    print(f'Su operación es: {number1} + {number2} = {resultado}')
    return historial.append(f'{number1} + {number2} = {resultado}')


def restar():
    number1 = get_minuendo() #float(input('Ingrese el minuendo: '))
    number2 = get_sustraendo() #float(input('Ingrese el sustraendo: '))
    resultado = number1 - number2 #resto o diferencia
    print(f'Su operación es: {number1} - {number2} = {resultado}')
    return historial.append(f'{number1} - {number2} = {resultado}')


def multiplicar():
    number1 = get_factor1() #float(input('Ingrese el primer factor: '))
    number2 = get_factor2() #float(input('Ingrese el segundo factor: '))
    resultado = number1 * number2
    print(f'Su operación es: {number1} x {number2} = {resultado}')
    return historial.append(f'{number1} x {number2} = {resultado}')


def dividir():
    number1 = get_dividendo() #float(input('Ingrese el dividendo: '))
    number2 = get_divisor() #float(input('Ingrese el divisor: '))
    resultado = number1 / number2
    #try:
    #    resultado = number1 / number2
    #except ZeroDivisionError:
    #    print('No se puede dividir por cero.')
    #    get_divisor()
    print(f'Su operación es: {number1} / {number2} = {resultado}')
    return historial.append(f'{number1} / {number2} = {resultado}')


def show_history():
    if not historial:
        print('\n No se realizaron cálculos.')
    else:
        print('\n *** Cálculos realizados: ***\n')
        for element in historial:
            print(element)
