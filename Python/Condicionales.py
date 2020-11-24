

""" #Estructura condicion
if condicion:
    codigo
elif condicion:
    codigo
elif condicion:
    codigo
else:
    codigo
     """
#Tipos de Condiciones > < >= <= != ==

fruta = input("Introduce una fruta:\n")
if fruta == "kiwi":
    print("La fruta es kiwi")
else:
    print("No son iguales")

#Otra forma de hacer el if
mensaje = "El Valor es kiwi" if fruta =="Kiwi" else "No son iguales"
print(mensaje)


if fruta == "kiwi":
    print("La fruta es kiwi")
elif fruta == "platano":
    print("La fruta es platano")
elif fruta == "durazno":
    #La palabra reservada pass se ocupa cuando para cierta condición no se ha definido un código. 
    pass
else:
    print("No son iguales")


#En python todas las estructuras vacias son falsas [], (), {}, "", None 
valor = ""

if valor:
    print("Es Verdad")
else:
    print("No es verdad")

#Palabras reservadas
# and, or, not