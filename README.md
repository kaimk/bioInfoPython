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
- Rechtsklicken sie auf Setup.py und auf Run unittest in setup.py 

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
