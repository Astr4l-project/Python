
#Funciones se crean con la palabra def
#La palabra reservada return "retorna" el valor de la función

def factorial_numero(numero):
    factorial = 1 
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


resultado = factorial_numero(5)
print(resultado)

def suma (valor_uno, valor_dos):
    return valor_uno + valor_dos

resultado = suma (10,50)
print(resultado)

#Definir funciones "n" argumentos
#Type retorna el tipo de clase
def suma_args(*args):
    print (args)
    #Retorna un tupla
    print (type(args))
    resultado = 0 
    for valor in args:
        resultado = resultado + valor
    return resultado

resultado = suma_args (10,50,50,6,7,8,10)
print(resultado)

#Definir funciones con "n" argumentos de tipo DICCIONARIO
def diccionario(**kwargs):
    #get devuelve el valor de buscado y en caso de no encontrarlo "No contiene valor"
    valor = kwargs.get('asdad', 'No contiene valor')
    return valor 

resultado = diccionario (valor = 'Eduardo', x=2, y=9, z = True)
print(resultado)

# * -> n valores -> tuplas
# ** -> n valores -> Diccionarios

################# Asignaciones

def division (valor_uno,valor_dos):
    return valor_uno/valor_dos

#Esta es otra forma de pasar los argumentos 
resultado = division (valor_dos = 10, valor_uno = 100)
print(resultado)

#Asignar valos por DEFAULT

def multiplicacion (valor_uno, valor_dos = 10): #Pasa por default si no se ingresa un segundo parametro
    return valor_uno * valor_dos

resultado = multiplicacion(6) #Se multiplica por 10 (DEFAULT)
print(resultado)

#Retornar multiples valores

def multiples_valores():
    return "String",1, True, 25.5

resultado = multiples_valores()
print(resultado) #Retorna una tupla

string = resultado[0]
entero = resultado[1]
bol = resultado [2]
floa = resultado [3]

print(string)
print(entero)
print(bol)
print(floa)

#Otra forma de hacer lo mimsmo es:

string, entero, bol, floa = multiples_valores()

print(string)
print(entero)
print(bol)
print(floa)

# ASIGNAR Y ANIDAR

#Asignar funciones a variable

mi_variable = multiplicacion
resultado = mi_variable(6)
print(resultado)

#Anidar funciones

def mostrar_resultado(funcion):
    print(funcion(5,6))
mostrar_resultado (mi_variable)
