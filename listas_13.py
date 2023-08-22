#suma de los elementos de una lista
#asume que las entradas son enteros
nums = input().split()
tot = 0
for n in nums:
	tot += int(n)
print(tot)