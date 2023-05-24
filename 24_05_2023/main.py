import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# print(df)
# df.plot()
#
# plt.legend()
# plt.show()

# x = np.random.randn(1000)
# plt.hist(x, bins=50, facecolor='c', alpha=0.75, density=True)
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamównienia'].sum()
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
#                                   autopvt=lambda pct: "{:.1f}%".format(pct),
#                                   textprops=dict(color="black"),
#                                   colors=['cyan','yellow'])
# plt.title('Suma zamówień dla sprzedawców')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()


# Przykład 1
sns.set(rc={'figure.figsize': (8,8)})
sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
             label='linia nr1', color='red', marker='o', linestyle=':')
sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17],
             label='linia nr2', color='cyan', marker='^',
linestyle=':')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres liniowy')
plt.show()

# Przykład 2

s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()
wykres = sns.relplot(kind='line', data=s, label='linia')
wykres.fig.set_size_inches(8,6)
wykres.fig.suptitle('Wykres liniowy losowych danych')
wykres.set_xlabels('indeksy')
wykres.set_ylabels('wartości')
wykres.add_legend()
wykres.figure.subplots_adjust(left=0.1, right=0.9,
bottom=-.1, top=0.9)
plt.show()

# Przykład 3
sns.set()
df = pd.read_csv('iris.data', header=0, sep=',',
 decimal='.')
print(df)
wykres = sns.lineplot(data=df, x=df.index, y='sepal length',
                      hue='class')
wykres.set_xlabel('indeksy')
wykres.set_title('Wykres liniowy danych z Iris Dataset')
wykres.legend(title='Rodzaj kwiatu')
plt.show()

# Przykład 4

sns.set()
data = {'a': np.arange(10),
        'c': np.random.randint(0, 50, 10),
        'd': np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d']) * 100
print(data['c'])
print(data['d'])
df = pd.DataFrame(data)
plot = sns.relplot(data=df, x="a", y="b", hue="c",
                  palette='plasma', size="d", legend=True)
plot.fig.set_size_inches(6, 6)
plot.set(xticks=data['a'])
plt.show()

# Przykład 5

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
sns.set()

plot = sns.barplot(data=df, x='Kontynent', y='Populacja',
ci=None, hue='Kontynent', estimator=np.sum, dodge=False, palette=['cyan','green','yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()