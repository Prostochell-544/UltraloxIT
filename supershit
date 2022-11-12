import math 
def perevod(a,b):
    if b== "байт":
        a=a*2**3
    elif b== "килобайт":
        a=a*2**13
    elif b== "мегабайт":
        a=a*2**23
    elif b== "гигабайт":
        a=a*2**33
    return a 
def it(N):
    T = int(math.log2(2*N-1))
    return T
def pamyat():
    N ="1 - Мощность алфавита, "
    K ="2 - колво символов в тексте, "
    I ="3 - информационный объём текста, "
    i ="0 - информация символа, "
    print("что нужно найти? (",i,N,K,I,")")
    what=input()
    if what=="0":
        N=(input("N-?\n"))
        K=int(input("K-?\n"))
        I,V=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if N=="":
            print(K*perevod(I,V))
        else: 
            print(it(int(N)))
    if what=="1":
        i=int(input("i-?\n"))
        print(2**i)
    if what=="3":
        K=int(input("K-?\n"))
        N=int(input("N-?\n"))
        i,V=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
             I=it(N)*K
        else:
            I=perevod(int(i),V)*K
        print(I)
    if what=="2":
        I,num=int(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        i,num2=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=int(input("N-?\n"))
        if i=="":
            K=perevod(I,num)/it(N)
        else:
            K=perevod(I,num)/perevod(int(i),num2)
        print(K)
def zvuk():
    N ="0 - количество уровней сигнала, "
    D ="1 - колво символов в тексте, "
    V ="2 - объём звуковоо файла, "
    i ="3 - глубина звука, "
    T ="4 - длительность звукового файла"
    print("Что нужно найти? (",N,D,V,i,T,")")
    G=input()
    if G=="0":
        i,b=int(input("i-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        print(2**perevod(i,b))
def isobr():
    print("isobr")
print("Какой тип задачи нужно решить? (звук, инфа, изобр)")
A=input()
if A=="звук":
    zvuk()
if A=="инфа":
    pamyat()
if A=="изобр":
    isobr()
import math


def perevod(a, b):
    if b == "байт":
        a = a * 2 ** 3
    elif b == "килобайт":
        a = a * 2 ** 13
    elif b == "мегабайт":
        a = a * 2 ** 23
    elif b == "гигабайт":
        a = a * 2 ** 33
    return a


def it(N):
    T = int(math.log2(2 * N - 1))
    return T


def pamyat():
    N = "1 - Мощность алфавита, "
    K = "2 - колво символов в тексте, "
    I = "3 - информационный объём текста, "
    i = "0 - информация символа, "
    print("что нужно найти? (", i, N, K, I, ")")
    what = input()
    if what == "0":
        N = (input("N-?\n"))
        K = int(input("K-?\n"))
        I, V = int(input("I-?\n")), input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if N == "":
            print(K * perevod(I, V))
        else:
            print(it(int(N)))
    if what == "1":
        i = int(input("i-?\n"))
        print(2 ** i)
    if what == "3":
        K = int(input("K-?\n"))
        N = int(input("N-?\n"))
        i, V = input("i-?\n"), input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i == "":
            I = it(N) * K
        else:
            I = perevod(int(i), V) * K
        print(I)
    if what == "2":
        I, num = int(input("I-?\n")), input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        i, num2 = input("i-?\n"), input("бит/байт/килобайт/мегабайт/гигабайт?\n")

        N = int(input("N-?\n"))
        if i == "":
            K = perevod(I, num) / it(N)
        else:
            K = perevod(I, num) / perevod(int(i), num2)
        print(K)


def zvuk():
    N = "0 - количество уровней сигнала, "
    D = "1 - Частота дискретизации, "
    V = "2 - объём звуковоо файла, "
    i = "3 - глубина звука, "
    T = "4 - длительность звукового файла"
    print("Что нужно найти? (", N, D, V, i, T, ")")
    G = input()
    if G == "0":
        V = input('V = ')
        M = input('M = ')
        I = input('I = ')
        t = input('t = ')
        print(f'k = {V / (I * M * t)}')
    if G == "1":
        I = input('I = ')
        M = input('M = ')
        t = input('t = ')
        k = input('k = ')
        print(f'V = {I * M * t * k}')
    if G == "2":


def isobr():
    print("isobr")


print("Какой тип задачи нужно решить? (звук, инфа, изобр)")
A = input()
if A == "звук":
    zvuk()
if A == "инфа":
    pamyat()
if A == "изобр":
    isobr()
