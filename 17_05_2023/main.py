import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plt.plot([1,3,5,7])
# plt.show()

# a = 2
# plt.plot([a**a,5,math.sqrt(5),7])
# plt.show()
#
# x = np.array([1,2,3,4])
# y = x**2

# plt.plot(x,y,'c')
# plt.plot(x,y,'o')
# plt.axis([0,6,0,20])
# plt.show()

# x = np.arange(0 , 5 ,0.2)
# plt.plot(x,x, 'c--', x, x**2, 'go', x, x**3, 'r^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'])
# plt.show()

# k = np.arange(0, 7, 0.3)
# plt.plot(k,k,'g-', label='liniowa')
# plt.plot(k, k**2, 'co-', label='kwadratowa')
# plt.plot(k,k**3,'r^--',label="sześcienna")
# plt.legend()
# plt.show()

# wykres funkcji sinus na przedziale x<0,10> wartości zmieniają
# się co 0.1

# x = np.arange(0, 10.1, 0.1)
# plt.plot(x, np.sin(x), 'co-', label='funkcja sinus')
# plt.legend(loc='best')
# plt.title('wykres funkcji sinus')
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)
#         }
# data['b'] = data['a'] + 10* np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='inferno')
# plt.xlabel('klucz a')
# plt.ylabel('klucz b')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(x1 * np.pi * 2)
# y2 = np.cos(x2 * np.pi * 2)
#
# plt.subplot(2, 1, 1)
# plt.plot(x1,y1)
# plt.title('Wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2,y2, 'r')
# plt.title('Wykres cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(x1 * np.pi * 2)
# y2 = np.cos(x2 * np.pi * 2)

# plt.subplot(4,1,1)
# plt.plot(x1, y1, 'c')
# plt.title('Wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(4,1,4)
# plt.plot(x2,y2, 'm')
# plt.title('Wykres cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.subplots_adjust(hspace=0.5)
#
# plt.show()


# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, 'g')
# axs[0, 0].set_title('wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('y')
#
# axs[1, 1].plot(x2, y2, 'b')
# axs[1, 1].set_title('wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('y')
#
# axs[2, 1].plot(x1, y1, 'r')
# axs[2, 1].set_title('wykres sin(x)')
# axs[2, 1].set_xlabel('x')
# axs[2, 1].set_ylabel('y')
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 0])
#
# plt.subplots_adjust(hspace=1.5)
#
# plt.show()


data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303170135, 207847528, 38675467]}
df = pd.DataFrame(data)
print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
#
# plt.bar(x=etykiety, height=wartosci, color=['yellow', 'red', 'cyan', 'green'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja')
# plt.show()

grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
print(grupa)

grupa.plot(kind='bar', xlabel='Kontynenty', ylabel='Populacja', legend=True, rot=0, title='Populacja na kontynentach')


plt.savefig('wykres.png')
plt.show()