p=int(input("p="))
np=int(input("N", p, "="))
k=1
N10=0
while np!=0:
    N10=N10+(np%10)*k
    k=k*p
    np=np//10
print("N10=",N10)