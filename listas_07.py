w = [2,8,10,9]
q = [9,10,2,3]
s = 0
for i in range(len(w)):
	s += w[i]*q[i]
print(s)

r = [9,10,"2",3]
s = 0
for i in range(len(w)):
	s += w[i]*r[i]
print(s)