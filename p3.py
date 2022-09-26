p=int(input())
for i in  range(1, p+1):
    for g in range(1, p+1):
        x=(i*g//10)*10+(i*g)%10
        print(x, end=' ')
    print()

