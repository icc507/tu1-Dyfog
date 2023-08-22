#Problema 3
#La entrada es una secuencia de números enteros
#La salida debe ser la suma de los números
#-----------------------
#Ejemplo de entrada
#10 2 8 20
#salida correspondiente
#40
#-----------------
#Por ahora la salida es sólo el primer número
#---------------------------------------------
lista = input().split()
nums = [int(eval(i)) for i in lista]
print(sum(nums))
