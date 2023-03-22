import random
#Zad1
liczby = [random.randint(0,30) for i in range(10)]
liczby2 = [ 2 * liczba for liczba in liczby]

with open("liczby.txt","w") as plik:
    for liczba in liczby2:
        plik.write(str(liczba) + "\n")
#Zad2
with open("liczby.txt",'r') as plik:
    lines = plik.readlines()

for line in lines:
    print(line.strip())
#Zad3
with open('przykładowy_tekst.txt', 'w', encoding='utf8') as f:
    f.write("Litwo! Ojczyzno moja! Ty DDjesteĹ jak zdrowie. NazywaĹ siÄ niedawno w wielkiej peruce, ktĂłrÄ do ojca Podkomorzego,")
    f.write("MoĹciwego Pana zastÄpuje i bagnami skradaĹ siÄ dowie kto go myĹlano do dworu. Tu KoĹciuszko w polskiej szacie")
    f.write("siedzi jak noga moja nie mogÄ. SĹoĹce ostatnich nie czytano w PaĹskim pisano zakonie i z Warszaw mam list, ")
    f.write("to mĂłwiÄc, Ĺźe nasi synowie i wrĂłciwszy w miechu. Starzy na to mĂłwiÄc, Ĺźe go kaznodziejÄ, Ĺźe zamczysko ")
    f.write("wziÄliĹmy w posiadĹoĹÄ. WszakĹźe kto ciÄ straciĹ. DziĹ czĹowieka rodu, obyczajĂłw! DoĹÄ, Ĺźe oko paĹskie jachaĹ ")
    f.write("szlachcic mĹody panek i juĹź to mĂłwiÄc, Ĺźe nasi synowie i nazwisko.")
with open('przykładowy_tekst.txt','r',encoding='utf8') as f:
    for line in f:
        print(line.strip())
#Zad4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyświetl_produkt(self):
        print(f"Nazwa produktu: {self.nazwa_produktu}")
        print(f"Ilość: {self.ilosc} {self.jednostka_miary}")
        print(f"Cena za jednostkę: {self.cena_jed} zł")
    def ile_produktu(self):
        return f"{self.ilosc} {self.jednostka_miary}"
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

ziemniaki = NaZakupy("ziemniaki", 5 , "kg", 2)

ziemniaki.wyświetl_produkt()
ziemniaki.ile_produktu()
ziemniaki.ile_kosztuje()
#Zad5
class CiagArytmetyczny:

    def __init__(self):
        self.wartosci = []

    def wyświetl_dane(self):
        print(self.wartosci)

    def pobierz_elementy(self):
        ilosc = int(input("Podaj ilość elementów: "))
        for i in range(ilosc):
            element = float(input(f"Podaj {i+1}. element: "))
            self.wartosci.append(element)

    def pobierz_parametry(self):
        pierwszy = float(input("Podaj pierwszy element: "))
        roznica = float(input("Podaj różnicę: "))
        ilosc = int(input("Podaj ilość elementów: "))
        self.wartosci = [pierwszy + i * roznica for i in range(ilosc)]

    def policz_sume(self):
        return sum(self.wartosci)

    def policz_elementy(self):
        pierwszy = self.wartosci[0]
        roznica = self.wartosci[1] - self.wartosci[0]
        ilosc = len(self.wartosci)
        ostatni = pierwszy + (ilosc - 1) * roznica
        return f"pierwszy: {pierwszy}, ostatni : {ostatni}, ilość : {ilosc}"


ciag1=CiagArytmetyczny()
ciag1.pobierz_parametry()
ciag1.wyświetl_dane()
print(ciag1.policz_sume())
print(ciag1.policz_elementy())
#Zad6
class Robaczek:
    def __init__(self, x , y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_pozycje_robaczka(self):
        print(f"Robaczek znajduje się na pozycji ({self.x}, {self.y})")

robaczek = Robaczek(0,0,5)
robaczek.pokaz_pozycje_robaczka()

robaczek.idz_w_gore(2)
robaczek.idz_w_prawo(3)
robaczek.idz_w_dol(1)
robaczek.idz_w_dol(4)

robaczek.pokaz_pozycje_robaczka()
