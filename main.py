import math
# zadanie1
print("||Zad1 =================================||")
print(math.pow(math.e,10))
print(math.pow(math.log(5+math.pow(math.sin(8),2),math.e),(1/6)))
print(math.floor(3.55))
print(math.floor(4.80))

# zadanie2
print("||Zad2 =================================||")
imie = "JAKUB"
nazwisko = "BACZEWSKI"
print(imie.capitalize(),nazwisko.capitalize())

# zadanie3
print("||Zad3 =================================||")
tekstPiosenki = "NANIMO NANIMO madashiraru"
print(tekstPiosenki.count("NANIMO"))

# zadanie4
print("||Zad4 =================================||")
lancuchoweSlowa = "ŁAŃCUSZEK"
print(lancuchoweSlowa[0],lancuchoweSlowa[8])

# zadanie5
print("||Zad5 =================================||")
losoweSlowa = "jakieś tam napisy śmieszne podzielone"
print(losoweSlowa.split())

# zadanie6
print("||Zad6 =================================||")
a = "txt"
b = float(37.17)
c = 320
print("%s" % a)
print("%f" % b)
print(hex(c))

# zadanie7
print("||Zad7 =================================||")
favSportsList = ["siatkówka","bieganie","pływanie","skoki w dal"]
print(favSportsList)
favSportsList.reverse()
favSportsList.append("Biatlon")
favSportsList.append("Jazda konna")
print(favSportsList)

# zadanie8
print("||Zad8 =================================||")
skrociki = {
    "idk": "i don't know",
    "nwm": "nie wiem",
    "cr?": "co robisz?",
    "nmzc": "nie ma za co",
    "dzk": "dzięki"
}
print(skrociki.keys())

# zadanie10
print("||Zad10 =================================||")

print("prosze napisz zdanie:\n")
zdanie = input()
print(zdanie.count("a"))

# zadanie9
print("||Zad9 =================================||")
games = {
    "mc": "minecraft",
    "F": "Fortnite",
    "pz": "Project zomboid",
    "bo3" : "call of duty black ops 3",
    "tarkov" : "escape from tarkov"
    }
print(games.keys())

# zadanie11
print("||Zad11 =================================||")
a1 = input()
b1 = input()
c1 = input()
maksimum = a1
if(b1 > maksimum):
    maksimum = b1
if(c1 > maksimum):
    maksimum = c1
print("największa liczba : " , maksimum)

# zadanie12
print("||Zad12 =================================||")

jakiesLiczbyFloat = [22.2,33.3,27.37,13.41]
print(jakiesLiczbyFloat)
for i in range (0,len(jakiesLiczbyFloat)):
    jakiesLiczbyFloat[i] *= jakiesLiczbyFloat[i]
print(jakiesLiczbyFloat)

# zadanie13
print("||Zad13 =================================||")
i = 0
parzyste = []
while i < 10:
    l = int(input("Podaj liczbe: "))
    if l % 2 == 0:
        parzyste.append(l)
    i += 1
print(parzyste)
