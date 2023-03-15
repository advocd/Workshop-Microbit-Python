# Visual Studio Code für micro:bit einrichten <!-- omit from toc --> 

- [Python und pip installieren](#python-und-pip-installieren)
  - [Ist Python bereits installiert?](#ist-python-bereits-installiert)
  - [Python Variante 1](#python-variante-1)
  - [Python Variante 2](#python-variante-2)
  - [pip](#pip)
- [uflash installieren](#uflash-installieren)
- [git installieren](#git-installieren)
- [VS Code Extensions installieren](#vs-code-extensions-installieren)
  - [Microsoft Python Extension](#microsoft-python-extension)
  - [micro:bit von Joseph Fergusson](#microbit-von-joseph-fergusson)


## Python und pip installieren

### Ist Python bereits installiert?
1. Terminal in VS Code öffnen.
2. Python Version abfragen. (z.B. `python -V`)
3. Wird eine Version ausgegeben, ist Python bereits installiert.
    Andernfalls muss Python installiert werden.

### Python Variante 1
Per Download von [python.org](https://www.python.org/downloads/)

### Python Variante 2
Per Kommandozeile. Befehle variieren abhängig vom Betriebssystem.

### pip
Pip ist der Paketmanager von Python. Er erlaubt es uns zusätzliche
Pakete zu installieren, die nicht in der Python-Standardbibliothek
enthalten sind.
Normalerweise wird pip bei der Installation von Python mit installiert. 
Ob das der Fall ist lässt sich mit `pip -V` überprüfen. Ist pip 
installiert wird die Version ausgegeben Andernfalls wird eine Anleitung 
zum Installieren ausgegeben. Dieser Anleitung folgen.

## uflash installieren
uflash (gesprochen micro-flash) erlaubt es uns, geschriebenen Code direkt 
auf den micro:bit zu laden.

`pip install uflash`

## git installieren
git ist eine freie Software zur Verwaltung von Dateiversionen. Sie erlaubt
es uns, den Verlauf von Änderungen an unserem Code zu sichern. Das heißt
beispielsweise, dass es möglich ist zu älteren Versionen zurückzukehren.
Außerdem können wir darüber auf Code anderer Entwickler*innen zugreifen.

1. Mit `git -V` überprüfen ob git bereits installiert ist.
2. Anleitung folgen, oder [herunterladen](https://git-scm.com/downloads)

## VS Code Extensions installieren

### Microsoft Python Extension
1. Im Reiter "Extensions" in der Suchleiste "Python" eingeben.
2. Microsoft Python Extension installieren.

### micro:bit von Joseph Fergusson
1. Im Reiter "Extensions" in der Suchleiste "microbit" eingeben.
2. micro:bit Erweiterung von Joseph Fergusson installieren.