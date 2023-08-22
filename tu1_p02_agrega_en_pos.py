#Problema 2 tutorial 1
#Para una secuencia con el siguiente significado
#Posición 0, un número que indica una posición p en la lista posterior
#Posición 1, un elemento e
#Posición 2 en adelante, una lista L separada por espacios
#Proceso esperado: El programa debe insertar en la posición p de la lista L el elemento e
#Si la posición p no existe debe agregarlo al final
#-----------------------------------------
#Ejemplo de entrada  2 q 10 20 30 40 50
#Ejemplo de salida ['10', '20', 'q', '30', '40', '50']
#------------------------------------------
#Ejemplo de entrada 9 w a b c
#Ejemplo de salida ['a', 'b', 'c', 'w']
#-------------------------------------
#Por ahora la lista entrega la lista completa (elementos en UNA línea separados por blanco)
entrada = input().split()
posicion = int(entrada[0])
elemento = entrada[1]

# Convertir los elementos restantes a una lista de cadenas
nueva_lista = entrada[2:]

# Convertir la posición a índice y verificar si está dentro de los límites
if posicion >= len(nueva_lista):
    nueva_lista.append(elemento)
else:
    nueva_lista.insert(posicion, elemento)

# Imprimir la nueva lista como cadenas
print(nueva_lista)
