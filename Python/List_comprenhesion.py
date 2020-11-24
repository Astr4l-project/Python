#Forma rápida para crear listas con valores (Lista_comprenhesion)
# 1- valor a agregar a la lista
# 2- un ciclo, for
lista = [valor for valor in range(0,101)]
print(lista)

#se pueden usar condiciones en las list comprenhesion
lista = [valor for valor in range(0,101) if valor % 2 ==0]
print(lista)

#Se pueden crear tuplas de la misma forma anterior
tupla = tuple ((valor for valor in range(0,101) if valor % 2 !=0))
print(tupla)

#Diccionarios
diccionario = {indice:valor for indice,valor in enumerate(lista)}
print(diccionario)

#diccionario con condicion
lista = [valor for valor in range(0,101)]
diccionario = {indice:valor for indice,valor in enumerate(lista) if indice <10}
print(diccionario)