lista = [1,2,3,4,5,6,7,8,9,10,11,13,16]

for valor in lista:
    pass

nuevo_rango = range(0,20,2)
for valor in nuevo_rango:
    pass

# valor = 0; valor < 20; valor = valor + 4
for valor in range(0,20,4):
    pass

#Enumerate devuelve el indice y el valor
for indice,valor in enumerate(lista):
    pass 
    #print(valor, "tiene el indice", indice)

#len devuelve la cantidad de items en un objeto iterable
for valor in range(0, len(lista)):
    pass
    #print(lista[valor])

#Los String son interables 
for valor in "Curso codigo facilito":
    pass
    #print(valor)

diccionario = {"a": 10, "b": 20, "c": 500}

#Diccionario.items() retorna un objeto iterable con un par clave, valor 
for clave, valor in diccionario.items():
    print ("La clave", clave,"tiene el valor de",valor)