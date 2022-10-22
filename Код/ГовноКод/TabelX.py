
p=int(input())
for i in  range(1, p+1):
    for g in range(1, p+1):
        x=(i*g//10)*10+(i*g)%10
        print(x, end=' ')
    print()
   


print("Основание системы")
p = int(input())
X = 1
Y = 1
for X in range(X,p):
	for Y in range(Y,p):
		Z = (X*Y //p)*10 + (X*Y)%p
		print(Z, end=" ")
	print()
	Y = 1
