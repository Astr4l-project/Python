contador = 0

while contador < 10: 
    print(contador)
    contador += 1 
    if contador ==5:
        #Termina el ciclo y salta al siguiente
        continue
    if contador ==6:
        #Termina el ciclo abruptamente
        break 
else:
    print("El While a Terminado")