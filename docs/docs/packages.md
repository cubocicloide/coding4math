# Packages

<div style="text-align: justify;">
In questa sezione vedremo come suddividere l'applicazione in moduli distribuiti in Python packages. Inoltre, mostreremo come importare e utilizzare packages (siano essi personali o di terze parti) all'interno di un programma.
</div>

---
## Organizzazione del codice

<div style="text-align: justify;">
Di solito non archiviamo tutti i file in una stessa locazione del nostro computer. Utilizziamo invece una gerarchia di directory ben organizzata per un accesso più semplice.

File simili sono conservati in una stessa directory, ad esempio si possono conservare tutti i brani nella directory musica. Analogamente, Python ha package per directory, e moduli per file.

Poiché la nostra applicazione potrebbe contenere un elevato numero di moduli, decidiamo di raggruppare quelli simili in un unico package e moduli diversi in package diversi. Ciò renderà l'applicazione facile da gestire e concettualmente più chiara.

Procedendo per analogia, così come una directory può contenere al suo interno altre directory e file, anche un package Python può avere al suo interno altri package e moduli.

Una directory, affinché sia considerata un package dall'interprete Python, deve contenere al suo interno un file chiamato <code>__init__.py</code>. Questo file può essere lasciato vuoto, in caso contrario conterrà al suo interno il codice di inizializzazione del package che lo contiene.<br>

&nbsp; Per facilitare la comprensione, proseguiamo la discussione introducendo un esempio. Supponiamo di stare sviluppando un gioco, allora una possibile organizzazione di package e moduli potrebbe essere la seguente.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/packages.svg" style="width: 500px;"><br>

</div>

---
## Importare moduli da packages

<div style="text-align: justify;">
Possiamo importare moduli da pacchetti usando l'operatore punto <code>.</code>.

Ad esempio, se si desidera importare il modulo <code>start</code> del package <code>Level</code> dell'esempio precedente, ciò può essere fatto mediante l'istruzione:
</div>
```
import Game.Level.start
```
<div style="text-align: justify;">
A questo punto, se tale modulo contiene una funzione <code>select_difficulty</code>, dovremo chiamarla utilizzando l'intero percorso che la individua:
</div>
```
Game.Level.start.select_difficulty()
```
<div style="text-align: justify;">
Se questo costrutto appare troppo lungo, possiamo importare il modulo senza il prefisso del package come segue:
</div>
```
from Game.Level import start
```
<div style="text-align: justify;">
di modo che adesso la chiamata alla funzione risulterà essere
</div>
```
start.select_difficulty()
```
<div style="text-align: justify;">
Un altro modo tramite cui importare solo la funzione richiesta (o la classe o la variabile) da un modulo all'interno di un package è il seguente:
</div>
```
from Game.Level.start import select_difficulty
```
<div style="text-align: justify;">
In tal caso, potremo chiamare direttamente la funzione come:
</div>
```
select_difficulty()
```
<div style="text-align: justify;">
Questo metodo di importare funzioni (o classi o variabili) è però soggetto a possibili conflitti tra identificatori identici che si riferiscono però a moduli diversi (ad esempio i packages <code>Sound</code> e <code>Level</code> contengono entrambi un modulo <code>load</code>).
</div>

---
## PyPI

<div style="text-align: justify;">
Il Python Package Index, detto anche <a href="https://pypi.org/" target="_blank">PyPI</a>, è una piattaforma su cui è possibile pubblicare e scaricare gratuitamente una vasta gamma di Python packages. Grazie al notevole sforzo della comunità Python, potremo in particolare usufruire di progetti che ci consentiranno un IoC (Inversion of Control) sul nostro applicativo, ovvero, in altri termini, ci eviteranno di re-inventare la ruota. Tra i diversi progetti che è possibile scaricare, vi sono ad esempio:
<ul>
<li><a href="https://pypi.org/project/numpy/" target="_blank">numpy</a>: consente la realizzazione di applicativi scientifici;</li>
<li><a href="https://pypi.org/project/matplotlib/" target="_blank">matplotlib</a>: rende possibile il plot di funzioni matematiche;</li>
<li><a href="https://pypi.org/project/tensorflow/" target="_blank">tensorflow</a>: permette di implementare algoritmi di Machine Learning;</li>
<li><a href="https://pypi.org/project/Django/" target="_blank">Django</a>: utile per sviluppare applicativi web;</li>
<li><a href="https://pypi.org/project/mkdocs/" target="_blank">mkdocs</a>: consente la realizzazione di guide come questo sito che state consultando.</li>
</ul>
Per capire l'utilità di questi progetti, forniamo come al solito un esempio. Supponiamo di voler eseguire il plot della funzione matematica seno. Possiamo allora fare affidamento sui package numpy e matplotlib. Il primo passo sarà includerli nel nostro ambiente virtuale, che allo stato iniziale è organizzato come segue: 
</div>
```
~
|__virtualenvs
   |__myvenv
      |__Include
      |__Lib
      |__Scripts
      |__pyvenv.cfg
      |__src
         |__main.py
```
<div style="text-align: justify;">
Per scaricare i package numpy e matplotlib all'interno del nostro ambiente virtuale, dovremo attivare l'ambiente virtuale e poi sfruttare l'utility <code>pip</code> messa a disposizione da Python:
</div>
```
(myvenv) src > pip install numpy
(myvenv) src > pip install matplotlib
```
<div style="text-align: justify;">
Come conseguenza, i package verranno scaricati nella directory <code>site-packages</code> dell'ambiente virtuale:
</div>
```
~
|__virtualenvs
   |__myvenv
      |__Include
      |__Lib
         |__python3.6
            |__site-packages
               |__numpy
               |__matplotlib
      |__Scripts
      |__pyvenv.cfg
      |__src
         |__main.py
```
<div style="text-align: justify;">
A questo punto potremo importare i moduli contenuti nei progetti numpy e matplotlib all'interno del nostro file <code>main.py</code>. In particolare, seguendo le istruzioni contenute nella documentazione ufficiale di <a href="https://matplotlib.org/" target="_blank">matplotlib</a>, potremo plottare la funzione seno inserendo nel nostro file <code>main.py</code> le seguenti istruzioni:
</div>
```
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)

ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x axis', ylabel='sin(x)',
       title='Plot')
ax.grid()

plt.show()
```
<div style="text-align: justify;">
ed eseguendolo come al solito. Per consentire la visualizzazione dell'output, riportiamo lo stesso script nella seguente shell interattiva. Lanciando il programma potrete visualizzare il plot della funzione seno.<br><br>
</div>

<div data-datacamp-exercise data-lang="python" data-height="200px" >
    <code data-type="sample-code" >
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)

ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x axis', ylabel='sin(x)',
       title='Plot')
ax.grid()

plt.show()
    </code>
</div> 



<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">


<script type="text/javascript" src="//cdn.datacamp.com/dcl-react.js.gz"></script>