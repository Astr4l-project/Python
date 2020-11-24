aux_var = "Hola Mundo"
print(aux_var) 

number_one = 10
number_two = 4

#  La función print, se puede escribir de la forma ("Str", variable) o ("Str", concatenar(variable))
result = number_one + number_two
print ("Suma", result)

result = number_one - number_two
print ("Resta", result)

result = number_one * number_two
print("Multiplicación", result)

result = number_one / number_two
print("Division",result)

result = number_one // number_two
print("División Entera", result)

result = number_one ** number_two
print("Exponencial", result)

result = number_one % number_two
print("Modulo", result)

#################### Strings ###############################

my_string = "Hola Mundo!\nMe llamo Astr4l\nMi objetivo es Ayudar al Mundo"
print(my_string)

course ="Python 3"
name ="Kevin"

final_message = "Nuevo curso de "+ course + " por " + name #1
print(final_message)
final_message = "Nuevo curso %s por %s" %(course,name) #2
print(final_message)
final_message = "Nuevo curso de {} por {}".format(course, name) #3 ---> Es la forma más elegante de trabajar
print(final_message)


my_string = "Curso de Código Facilito!"

print(my_string)
print(my_string[0])

#El signo negativo invierte el sentido de lectura
print(my_string[-1])

#Extrae --> posinicial:posfinal+1
print(my_string[0:10])

#Extrae con saltos --> posinicial:posfinal+1:salto
print(my_string[0:10:2])

#Hacer un reverse a un String ::-1
print(my_string[::-1])


### Métodos String #### 

#FORMATOS#

course = "Curso"
my_string = "Código Facilito"

result = "{} de {}".format(course,my_string)
print(result)

#Este formato parece útil 
result = "{a} de {b}".format(b = course, a= my_string)
print(result)

#Minisculas
print(result.lower())

#Mayusculas
print(result.upper())

#Titulos
print(result.title())


#BUSQUEDA# 

#El metodo find devuelve -1 cuando no encuentra el valor 
pos = result.find("Curso")
print(pos)

#Cuenta los caracteres
count = result.count("o")
print(count)

#REEMPLAZO

#Donde esta "o" reemplaza con X  
new_string = result.replace ("o","x")
print(new_string)


#SPLIT
new_string = result.split(" ")
print(new_string)