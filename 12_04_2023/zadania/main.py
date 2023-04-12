import numpy as np

print("============= Zad 1 =================")
tablica = np.arange(1, 20, 4)
print(tablica)

print("============= Zad 2 =================")

a = np.arange(1, 4, 0.1)
print(a)
b = a.astype('int32')
print(b)
print(b.dtype)

print("============= Zad 3 =================")

def wymiar(n):
    l = 2
    m = np.zeros([n,n],dtype='int64')
    for i in range(n):
        for j in range(n):
            m[i,j] = l
            l *= 2
    return m
print(wymiar(5))

print("============= Zad 4 =================")

def zad4(podstawa, ilosc):
    m = np.arange(ilosc)
    for i in range(ilosc):
        m[i] = podstawa**(i+1)
    return m

a1 = zad4(2,4)
b2 = zad4(3,5)

print(a1)
print(a2)

