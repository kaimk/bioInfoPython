# bioInfoPython
Willkommen zum python tutorial.
Um zu naechsten tutorial zu gelangen führen sie alle Aufgaben aus
und lassen sie die Tests laufen.
Wenn alle Tests erfolgreich waren benutzen sie git pull um das Projekt zu updaten.

Tutorial 1 - setup
- (Falls Python 2.7 noch nicht auf ihrem Rechner installiert ist) Installieren sie Pyhton 2.7.X von https://www.python.org/downloads/
- (Falls PyCharm noch nicht auf ihrem Rechner installiert ist) Installieren sie PyCharm von https://www.jetbrains.com/pycharm/
- Oeffnen sie die datei setup.py in PyCharm
- Stellen sie den Pyhton interpreter von PyCharm auf die installierte Python 2.7 version. (File -> settings -> Project:Setup.py -> Project interpreter)
- Rechtsklicken sie auf tests.py und auf Run unittest in tests.py

Tutorial 2 - variables
In Python werden Variablen definiert indem ihnen ein Wert zugewiesen wird.
Beispiel:
meine_variable = 3
Ab jetzt einhaelt meine_variable den Wert 3.
Da Python eine dynamische Sprache ist braucht der Typ der Variable nicht angegeben zu werden,
deshalb kann auf die gleiche Weise auch ein String in einer Variable gespeichert werden:
meine_string_variable = "ATTCGGCT"
Statt der doppelten Anführungszeichen (" ") koennen auch einfache (' ') verwendet werden.
Variablen die Zahlen enthalten koennen mit den ueblichen methoden (+, -, , /) manipuliert werden.
Beispiel:
var1 = 5
var2 = meine_variable + var1
var2 enthaelt jetzt den Wert 3 + 5 = 8

Erstellen sie im gleichen Verzeichnis in dem sich auch die Datei setup.py einen Ordner names src.
Erstellen sie im src Ordner die datei __init__.py (Das ist ein Technischens detail das jetzt unwichtig ist)
Erstellen sie im src Ordner die datei variablen.py
Oeffnen sie diese Datei mit pycharm.
- erstellen sie eine Variable var1 mit dem wert 4
- erstellen sie eine Variable var2 mit dem wert 5
- erstellen sie eine Variable var3 und weisen sie ihr die summe von var1 und var2 zu. (Benutzen sie dazu die Variablen nicht die Werte 4 und 5)
- erstellen sie eine Variable s1 mit dem Wert "ATCG"
- erstellen sie eine Variable s2 mit dem Wert "GCTA"
- erstellen sie eine Variable s3 = s1 + s2
- geben sie den Wert von s3 mit print(s3) aus
- erstellen sie eine Variable s4 = s1+str(var1) und geben sie das ergebnis aus

Sie koennen die Datei variablen.py ausführen indem sie rechtsklicken -> Run variablen.py
Rechtsklicken sie auf tests.py -> Run "Unitests in tests.py"

Tutorial 3 - Listen
Will man ein Programm schreiben das viele Variablen enthaelt ist es
sehr unpraktisch jede dieser variablen einzeln zu deklarieren.
Python (alle anderen Programmiersprachen auch) hat für diesen Zweck Listen.
In Python werden Listen mit eckigen Klammern definiert:
meine_liste = [4, 5, 6]
Strings können genauso in Listen gespeichert werden:
meine_zweite_liste = ["abc", "def", "ghi"]
ausserdem können Listen Listen enthalten:
meine_2d_liste = [[1,2],[3,4]]
So kann man z.B.: Matrizen darstellen.
Auf die Elemente der Liste wird mit den eckigen Klammern zugegriffen
meine_liste[0] gibt den Wert 4 zurück (Listen fangen bei 0 an zu zählen
meine_liste hat die indizes 0,1,2).
Eine weitere Methode variablen zusammen zu fassen sind dictionaries.
In einem dictionary werden die einzelnen Werte über Schlüssel angesprochen.
Geschweifte Klammern definiern ein dictionary:
mein_dict = {"eins" : 1, "zwei" : 2, "drei" : 3}
mein_dict["eins"] gibt den Wert 1 zurück

- erstellen sie im src ordner die datei lists.py
- erstellen sie eine Liste meine_liste mit den Werten 1 bis 9
- weisen sie den Wert mit index 3 der variable var1 zu
- erstellen sie ein dictionarie mein_dict mit den Schlüsseln "a", "b", "c"
    mit den Werten a = 4, b = 5, c = 6
- weisen sie den Wert von "b" der Variable var2 zu
( wenn sie wollen koennen sie den inhalte von meine_liste und mein_dict
mit print(meine_liste) und print(mein_dict) ausgeben)
Sie koennen die Datei lists.py ausführen indem sie rechtsklicken -> Run lists.py
Rechtsklicken sie auf tests.py -> Run "Unitests in tests.py"

Tutorial 4 - Schleifen
Hat man eine Liste mit 1000 Werten ist es natuerlich sehr muehsam
auf alle per Hand zu zugreifen. Um Listen zu "durchlaufen" gibt es
Schleifen. Python unterstuetzt sowohl for Schleifen als auch while Schleifen.
Der Syntax fuer for schleifen ist:
for variable in ...:
    mach etwas mit variable
dabei muss alles was in der Schleife wiederholt werden soll eingerueckt sein
Beispiel
for i in range(0, 3):
    print(i)
print("hallo")

Das Beispiel gibt die Zahlen 0, 1, 2, 3 aus
hallo wird nur einmal ausgegeben weil es wegen der einrueckung nicht mehr zur Schleife gehoert.
In einer Schleife kann man auch Listen füllen:
meine_liste = []
for i in range(0, 3):
    meine_liste.append(i)
print(meine_liste)
gibt: [0,1,2,3]

while Schleifen laufen solange eine Bedingung wahr ist:
var1 = 1
while var1 <= 5:
    print(var1)
    var1 = var1 + 1
solange die variable var1 kleiner oder gleich 5 ist wird der inhalt der Variable ausgegeben
und danach wird var1 um 1 erhoeht.

- erstellen sie im ordner src eine datei schleifen.py
- erstellen sie eine leere Liste meine_liste
- fuellen sie meine_liste in einer for Schleife mit den Werten 1 bis 100
- erstellen sie eine variable var1 = 1
- solange var1 kleiner oder gleich 20 ist erhoehen sie var1 um den Wert von var1 (var1 = var1 + var1)

Sie koennen die Datei schleifen.py ausführen indem sie rechtsklicken -> Run schleifen.py
Rechtsklicken sie auf tests.py -> Run "Unitests in tests.py"
