
############ LISTAS #####################

#Instancia

my_list = ["Strings", 15, 15.6, True]
print(my_list)

#Agregar al final

my_list.append(6)
print(my_list)

#Insertar

my_list.insert(1,"Insert")
print(my_list)

#Remover
my_list.remove(15)
print(my_list)

#Remover como Pila

list_value = my_list.pop()
print(list_value)
print(my_list)

#Ordenar de menor a mayor
my_list = [1,9,22,6,7,65,14,99]
my_list.sort()
print(my_list)

#Ordenar de mayor a menor
my_list = [1,9,22,6,7,65,14,99]
my_list.sort(reverse=True)
print(my_list)

#Concatenar listas (al final)
my_list = [1,9,22,6,7,65,14,99]
my_list_two = [22,23]
my_list.extend(my_list_two)
print(my_list)

