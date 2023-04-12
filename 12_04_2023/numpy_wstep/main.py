import numpy as np
# inicjalizacja tablicy
a = np.array([[0,1],[2,3]])
print(a)
# lub drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
# wypisywanie typu zmiennej tablicy (nie jej elementów)
print(type(a))
# sprawdzanie typu danych tablicy
print(a.dtype)
# inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)
# zapisywanie kopii tablicy jako tablicy z innym typem
#b = a.astype()
#print(b)
#print(b.type)
#wypisywanie rozmiaru tablicy
#print(b.shape)
#ilość wymiarów tablicy
#print(a.ndim)
# tworzenie tablicy wielowymiarowej
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
# ponownie typem jest ndarray
print(type(m))

zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera.dtype)
print(jedynki.dtype)
# macierz pusta
pusta = np.empty((2,2))
print(pusta)

liczby_lin = np.linspace(1,2,5)
print(liczby_lin)
liczby_lin2 = np.linspace(1,2,5,endpoint=False)
print(liczby_lin2)

z = np.fromiter(range(5), dtype='int32')


# znaki
znaki = b'ogolna'
z1 = np.frombuffer(znaki,dtype='S1')
print(z1)
z2 = np.frombuffer(znaki,dtype='S3')
print(z2)

znaki1 = 'ogolna'
z3 = np.array(list(znaki1))
z4 = np.array(list(znaki1), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki,dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
s = range(2,7,2)
print(a[s])

print(a[2:7:2])

print(a[1:])
print(a[2:5])

mat = np.arange(25)
mat = mat.reshape((5,5))
print(mat)
print(mat[1:])
print(mat[:,1])
print(mat[:,-1])


x = np.array([[0,1,2], [3,4,5], [6,7,8], [9,10,11]])
print(x)
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2], [0,2]])
y = x[rows,cols]
print(y)









