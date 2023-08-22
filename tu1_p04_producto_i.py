#Problema 4 tutorial 1
#Para una secuencia de números
#Programe el producto interior (elemento a elemento)
#de los números en las posiciones pares respecto de las impares
#(los elementos que faltan deben ser 0) 
#-------------------------------------------------------------
#Ejemplo de Entrada
# 1 2 3 6 2
# debe consierarse (1 3 2) . (2 6 0) = 1x2 + 3x6 + 2x0 = 20
#Ejemplo de salida 20
#-------------------------------------
#Por ahora la lista entrega los elementos pares agregado un cero
lista = input().split()[0::2]+[0]
print(lista)
