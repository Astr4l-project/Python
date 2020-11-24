

#Son de forma key:value (Donde la clave debe ser inmutable Ej. String, tuplas y enteros)

#Instancia
diccionario = { "a" : 55, 5: "String", (1,2): False}
print(diccionario)

#Si se repite una llave, toma la última (pila)
diccionario = { "a" : 55, 5: "String", "a": False}
print(diccionario)

#Agregar/Modificar ---> diccionario[key] = value
diccionario["c"] = "Nuevo String"
print(diccionario)
diccionario["a"] = True
print(diccionario)

#Obtener valor

valor = diccionario["c"]
print(valor)

#Método Get. busca la clave y devuelve un valor default (find,default)

valor = diccionario.get("z",False)
print(valor)

valor = diccionario.get("c",False)
print(valor)

#Remover ---> Sufijo del 

del diccionario[5]
print(diccionario)

#Lista de llaves
diccionario = { "a" : 55, 5: "String", (1,2): False}
llaves = diccionario.keys()
print(llaves)

#Lista de valores
valores = list(diccionario.values())
print(valores)

#Casting para lista pura
llaves = list(diccionario.keys())
print(llaves)

#Casting para una tupla
llaves = tuple(diccionario.keys())
print(llaves)


#Extender diccionario 

#Metodo 1
diccionario = { "a" : 55, 5: "String", (1,2): False}
diccionario_dos = {"z":23, "w":88}

diccionario["z"] = diccionario_dos["z"]
diccionario["w"] = diccionario_dos["w"]

print(diccionario)

#Metodo 2 ---> Update (USAR ESTE)
diccionario = { "a" : 55, 5: "String", (1,2): False}
diccionario_dos = {"z":23, "w":88}

diccionario.update(diccionario_dos)
print(diccionario)