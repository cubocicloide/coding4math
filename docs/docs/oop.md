# Object Oriented Programming

<div style="text-align: justify;">
La Programmazione Orientata agli Oggetti, detta anche OOP, è un paradigma di programmazione che fornisce un mezzo per strutturare i programmi in modo che le proprietà e i comportamenti siano raggruppati in singoli oggetti. <br>
&nbsp; Ad esempio, un oggetto potrebbe rappresentare un'azienda le cui proprietà siano ragione sociale e partita IVA, e i cui comportamenti siano acquistare, produrre e vendere. Oppure un oggetto potrebbe essere una e-mail con proprietà quali elenco di destinatari, oggetto e corpo, e comportamenti quali aggiunta di allegati e invio. <br>
&nbsp; In altre parole, la OOP è un approccio per la modellazione di oggetti concreti, come automobili e relazioni tra aziende e dipendenti, studenti e insegnanti, e via di seguito. Tramite la OOP si cerca quindi di modellare il mondo reale attraverso oggetti che posseggono alcuni dati associati all'entità reale, e che possono svolgere determinate funzioni.
</div>

---
## Classi
<div style="text-align: justify;">
Nell'introduzione abbiamo visto che gli oggetti sono l'elemento cardine della OOP. In termini più specifici, ogni oggetto è l'istanza di una classe. Cerchiamo quindi di capire cosa è una classe e come è possibile istanziarla.<br>
&nbsp; Iniziamo considerando alcuni tipi di variabili standard disponibili in Python, come numeri, stringhe e liste. Questi sono progettati per rappresentare, rispettivamente, cose semplici come il costo di un bene, la descrizione dello stesso, o un elenco di prodotti. Ma se invece vogliamo rappresentare qualcosa di più complicato, come possiamo fare?<br>
&nbsp; La risposta è utilizzare le classi. Queste, infatti, sono utilizzate per creare nuovi tipi di dati definite dal programmatore, che contengono attributi (dette anche proprietà) e metodi arbitrari di una data entità reale. Ad esempio, se l'entità considerata è un poligono, la sua classe può ad esempio possedere come attributi la sua base e la sua altezza, e come metodi una descrizione formale dello stesso.
&nbsp; La sintassi prevista per definire una classe è la seguente:
</div>
```python
class NomeClasse:
    blocco class
```
<div style="text-align: justify;">
In particolare, la definizione di una classe ha le seguenti componenti:
<ul>
<li>la parola chiave <code>class</code>, che contrassegna l'inizio dell'intestazione della classe;</li>
<li>un nome di classe che la identifica in modo univoco (si noti che, per convenzione, il nome va scritto usando la notazione CamelCase);</li>
<li>due punti <code>:</code> per contrassegnare la fine dell'intestazione della classe;</li>
<li>un blocco di codice opportunamente indentato che conterrà attributi e metodi della classe;</li>
</ul>
Immaginiamo di voler trattare, come entità reale, i poligoni. Allora un esempio di classe che li rappresenti è il seguente:
</div>
```python
class Poligono:
    pass
```
<div style="text-align: justify;">
dove, per il momento, lasciamo in sospeso la creazione del <code>blocco class</code> attraverso la keyword <code>pass</code>.
</div>

---
## Oggetti
<div style="text-align: justify;">
Abbiamo già detto che un oggetto è istanza di una classe. A questo punto, ci chiediamo quindi come è possibile istanziare una classe, la qual cosa è molto semplice. Infatti sarà sufficiente creare una nuova variabile a cui assegnare il valore <code>NomeClasse()</code>. Ad esempio, considerando la classe <code>Poligono</code> di cui sopra, una sua istanza è la seguente:
</div>
```python
pol = Poligono()
```
<div style="text-align: justify;">
In questo caso, abbiamo creato l'oggetto <code>pol</code> che, in particolare, è una istanza della classe <code>Poligono</code>.
</div>

---
## Attributi

<div style="text-align: justify;">
Finora, la classe <code>Poligono</code> non descrive affatto le caratteristiche dell'entità reale che rappresenta. Infatti, ogni poligono dispone di alcuni attributi che lo contraddistinguono, ad esempio il tipo, l'altezza e la base. Occorre quindi introdurre questi attributi all'interno della relativa classe. Per farlo, si impiega il metodo speciale <code>__init__()</code>, anche detto metodo costruttore della classe. Quest'ultimo è in sostanza una funzione che serve a inizializzare gli attributi di un oggetto assegnando loro un valore (di default o specificato dall'utente). Proseguendo col nostro esempio, avremo in particolare che:
</div>
```python
class Poligono:
    def __init__(self, tipo, base, altezza):
        """
        Metodo speciale necessario a inizializzare gli attributi della classe.
        """
        self.tipo = tipo
        self.base = base
        self.altezza = altezza
```
<div style="text-align: justify;">
Esaminiamo il codice appena introdotto. Notiamo che la funzione <code>__init__()</code> possiede i seguenti parametri di input:
<ul>
<li><code>self</code>: è una keyword con la quale si identifica una generica istanza della classe;</li>
<li><code>tipo</code>, <code>base</code>, <code>altezza</code>: sono gli attributi della classe.</li>
</ul>
All'interno della funzione <code>__init__()</code> si ripete poi la sintassi <code>self.nome_attributo = nome_attributo</code>. Il significato di questa istruzione è il seguente: considera la generica istanza della classe <code>Poligono</code>, identificata con la keyword <code>self</code>, e assegnagli come attributi i valori specificati in input.<br>
&nbsp; A questo punto, potremo creare un oggetto poligono, visualizzare i valori dei suoi attributi ed eventualmente modificarli:
</div>
```python
pol = Poligono(tipo = 'triangolo', base = 3, altezza = 5)

# stampiamo i valori degli attributi di pol
print('tipo: {0}, base: {1}, altezza: {2}'.format(pol.tipo, pol.base, pol.altezza))

# modifichiamo gli attributi di pol
pol.tipo = 'rettangolo'
pol.base = 2
pol.altezza = 1

# stampiamo i nuovi valori degli attributi di pol
print('tipo: {0}, base: {1}, altezza: {2}'.format(pol.tipo, pol.base, pol.altezza))
```
<div style="text-align: justify;">
L'output prodotto dallo script sarà:
</div>
```
tipo: triangolo, base: 3, altezza: 5
tipo: rettangolo, base: 2, altezza: 1
```

---
## Metodi

<div style="text-align: justify;">
Le classi, oltre agli attributi, si compongono di metodi che descrivono i comportamenti dei suoi oggetti. In pratica, i metodi non sono nient'altro che funzioni definite all'interno della classe. Nella sottosezione precedente abbiamo già visto il metodo speciale <code>__init__()</code>, usato per inizializzare gli attributi della classe. Tra i metodi speciali più importanti, vi è anche il metodo <code>__str__()</code>, il quale ci consente di fornire una descrizione informale dell'oggetto. Volendo implementare tale metodo per la classe <code>Poligono</code>, potremmo ad esempio fornire una stampa contenente il valore dei suoi attributi: 
</div>
```python
class Poligono:
    def __init__(self, tipo, base, altezza):
        """
        Metodo speciale necessario a inizializzare gli attributi della classe.
        """
        self.tipo = tipo
        self.base = base
        self.altezza = altezza

    def __str__(self):
        """
        Metodo speciale che consente di fornire una descrizione informale della classe.
        """
        print('Il poligono considerato è un {0}.'.format(self.tipo))
        print('Base: {0}. Altezza: {1}.'.format(self.base, self.altezza))
```
<div style="text-align: justify;">
Dato un oggetto poligono, denominato <code>pol</code>, si potrà chiamare il metodo <code>__str__()</code> tramite la sintassi che segue:
</div>
```python
pol = Poligono('triangolo',3,4)
pol.__str__()
```
<div style="text-align: justify;">
L'output prodotto sarà:
</div>
```
Il poligono considerato è un triangolo.
Base: 3. Altezza: 4.
```
<div style="text-align: justify;">
Più in generale, data la classe <code>Classe</code>, un suo metodo <code>metodo()</code> e una sua istanza <code>oggetto</code>, potremo chiamare il <code>metodo()</code> sull'istanza <code>oggetto</code> attraverso la sintassi:
</div>
```python
oggetto.metodo()
```
<div style="text-align: justify;">
Terminiamo la sottosezione dicendo che, oltre ai metodi speciali, ci sono ovviamente i metodi personalizzati definiti dal programmatore, come vedremo nella prossima sottosezione. 
</div>

---
## Principi della OOP

<div style="text-align: justify;">
Abbiamo introdotto gli elementi cardine della OOP, ossia le classi (che si compongono di attributi e metodi) e gli oggetti (che sono istanze delle classi). In questa sottosezione, ci occuperemo invece di dare una brevissima descrizione dei principi che sono alla base del paradigma di programmazione OOP, ovvero:
<ul>
<li>Incapsulamento</li>
<li>Ereditarietà</li>
<li>Astrazione</li>
<li>Polimorfismo</li>
</ul>
</div>

---
### Incapsulamento

<div style="text-align: justify;">
L'incapsulamento è quella pratica, consueta nella OOP, tramite cui si impedisce, all'utente finale, di avere accesso diretto agli attributi di un oggetto. Per capire meglio, proseguiamo con l'esempio relativo alla classe <code>Poligono</code>. Allo stato attuale, nessuno impedisce all'utente di istanziare un <code>Poligono</code> il cui tipo è indefinito, oppure che abbia base o altezza negativa. Infatti, eseguendo:
</div>
```python
pol = Poligono('pinco_pallino',-3,-4)
pol.__str__()
```
<div style="text-align: justify;">
otterremo l'output:
</div>
```
Il poligono considerato è un pinco_pallino.
Base: -3. Altezza: -4.
```
<div style="text-align: justify;">
ossia, il programma, pur sintatticamente corretto, è semanticamente scorretto, in quanto nella realtà non vi è alcun poligono <code>pinco_pallino</code>, nè tantomeno poligoni che abbiano base o altezza negativa. Per correggere l'errore semantico, dobbiamo limitare l'accesso agli attributi della classe, e per farlo, dobbiamo impiegare dei metodi noti in letteratura come metodi getter e setter. Nel linguaggio Python, l'implementazione di tali metodi avviene tramite il <a href="https://gist.github.com/Zearin/2f40b7b9cfc51132851a" target="_blank">decoratore</a> integrato <code>@property</code>. Nel nostro caso, i metodi getter e setter, per ciascun attributo, dovranno occuparsi di verificare che i valori inseriti dall'utente siano corretti. La classe sarà quindi modificata come segue:
</div>
```python
class Poligono:
    def __init__(self, tipo, base, altezza):
        self.tipo = tipo
        self.base = base
        self.altezza = altezza

    def __str__(self):
        print('Il poligono considerato è un {0}.'.format(self.tipo))
        print('Base: {0}. Altezza: {1}.'.format(self.base, self.altezza))

    @property
    def tipo(self):
        """
        Questo metodo, di tipo getter, restituisce il valore dell'attributo tipo.
        """
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        """
        Questo metodo, di tipo setter, si occupa di stabilire se l'utente ha inserito un 
        tipo corretto di poligono. In tal caso, gli unici tipi ammessi sono 
        triangolo e rettangolo. Se il valore è corretto, il tipo viene 
        assegnato al corrispondente attributo, altrimenti viene sollevata un'eccezione.
        """
        if tipo not in ('triangolo', 'rettangolo'):
            raise ValueError('[ERROR] Il tipo di poligono inserito non è supportato.')
        else:
            self._tipo = tipo
    
    @property
    def base(self):
        """
        Questo metodo, di tipo getter, restituisce il valore dell'attributo base.
        """
        return self._base
    @base.setter
    def base(self, base):
        """
        Questo metodo, di tipo setter, si occupa di verificare se l'utente ha inserito
        una base positiva. Se il valore è corretto, la base viene assegnata al 
        corrispondente attributo, altrimenti viene sollevata un'eccezione.
        """
        if base <= 0:
            raise ValueError('[ERROR] La base non può essere minore o uguale a 0.')
        self._base = base

    @property
    def altezza(self):
        """
        Questo metodo, di tipo getter, restituisce il valore dell'attributo altezza.
        """
        return self._altezza
    @altezza.setter
    def altezza(self, altezza):
        """
        Questo metodo, di tipo setter, si occupa di verificare se l'utente ha inserito
        un'altezza positiva. Se il valore è corretto, l'altezza viene assegnata al
        corrispondente attributo, altrimenti viene sollevata un'eccezione.
        """
        if altezza <= 0:
            raise ValueError("[ERROR] L'altezza non può essere minore o uguale a 0.")
        self._altezza = altezza
```
<div style="text-align: justify;">
A questo punto, avendo ridefinito la classe, se eseguiamo lo script:
</div>
```python
try:
    pol = Poligono('pinco_pallino',-3,-4)
except ValueError as error:
    print(error)       
else:
    triangolo.__str__()
```
<div style="text-align: justify;">
verrà restituito in output il seguente messaggio di errore:
</div>
```
[ERROR] Il tipo di poligono inserito non è supportato.
```
<div style="text-align: justify;">
Pertanto, l'utilizzo dei metodi getter e setter ha reso possibile un controllo sui dati inseriti dall'utente, di modo che il programma risulti semanticamente corretto.
</div>

---
### Ereditarietà

<div style="text-align: justify;">
L'ereditarietà è il processo mediante il quale una classe assume gli attributi e i metodi di un'altra classe. Le classi di nuova formazione verranno dette classi child, mentre le classi da cui derivano verranno dette classi parent. Proseguendo col nostro esempio, abbiamo impostato la classe <code>Poligono</code> di modo che descriva due tipi: i triangoli e i rettangoli. In particolare, potremmo voler definire una classe <code>Triangolo</code> che derivi dalla classe <code>Poligono</code>. In tal caso, basterà usare la sintassi:
</div>
```python
class Triangolo(Poligono):
    pass
```
<div style="text-align: justify;">
In particolare, <code>Triangolo</code> sarà la classe child di <code>Poligono</code>, mentre <code>Poligono</code> sarà la classe parent di <code>Triangolo</code>.<br> 
&nbsp; Per dare maggiore senso alla classe <code>Triangolo</code>, estendiamo i metodi speciali <code>__init__()</code> e <code>__str()___</code> della sua classe parent, e lo facciamo tramite la funzione integrata <code>super()</code><sup><a href="#fn0" id="ref0">1</a></sup>:
</div>
```python
class Triangolo(Poligono):
    def __init__(self, base, altezza):
        super().__init__(tipo = 'triangolo', base = base, altezza = altezza)

    def __str__(self):
        super().__str__()
```
<div style="text-align: justify;">
Giunti qui, lanciando il seguente script:
</div>
```python
try:
    triangolo = Triangolo(3,4)
except ValueError as error:
    print(error)       
else:
    triangolo.__str__()
```
<div style="text-align: justify;">
otterremo l'output:
</div>
```
Il poligono considerato è un triangolo.
Base: 3. Altezza: 4.
```
<div style="text-align: justify;">
Si noti in particolare che la classe <code>Triangolo</code> ha ereditato per intero i metodi getter e setter della sua classe parent, inoltre ha esteso i metodi <code>__init__()</code> e <code>__str__()</code> della sua classe parent. La cosa importante da ricordare è che le classi child ereditano tutti gli attributi e i metodi delle relative classi parent, e hanno la possibilità di modificarli e di aggiungerne di nuovi.
</div>

---
### Astrazione

<div style="text-align: justify;">
Ci occupiamo ora di astrazione, fornendo subito un esempio. Tutti noi sappiamo che è possibile il calcolo dell'area di un poligono, tuttavia la formula dell'area dipende dal tipo di poligono considerato. In altre parole, sappiamo in astratto come calcolare l'area di un poligono a patto di conoscerne il tipo, ad esempio un triangolo o un rettangolo; ovvero, nota la classe child del <code>Poligono</code>, possiamo determinarne l'area.<br>
&nbsp; Per accertarsi che ciascuna classe child implementi il calcolo dell'area, bisognerà allora dichiarare come astratta la classe <code>Poligono</code>, e definire un suo metodo astratto che sia predisposto al calcolo dell'area, una volta nota una sua classe child. A tal fine, il linguaggio Python mette a disposizione il modulo <code>abc</code>, da cui è possibile importare la classe <code>ABC</code> e la funzione <code>abstractmethod</code>:
</div>
```python
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, tipo, base, altezza):
        self.tipo = tipo
        self.base = base
        self.altezza = altezza

    def __str__(self):
        print('Il poligono considerato è un {0}.'.format(self.tipo))
        print('Base: {0}. Altezza: {1}.'.format(self.base, self.altezza))

    @abstractmethod
    def area(self):
        pass
```
<div style="text-align: justify;">
Si noti in particolare che la classe <code>Poligono</code> è ora una classe child di <code>ABC</code>, e che il suo metodo <code>area()</code> è stato dichiarato astratto mediante il decoratore <code>@abstractmethod</code>. A questo punto, eseguendo lo script:
</div>
```
try:
    triangolo = Triangolo(3,4)
except ValueError as error:
    print(error)       
else:
    triangolo.__str__()
```
<div style="text-align: justify;">
verrà sollevata la seguente eccezione <code>TypeError</code>
</div>
```
Traceback (most recent call last):
  File "main_1.py", line 65, in <module>
    main()
  File "main_1.py", line 58, in main
    triangolo = Triangolo(3,4)
TypeError: Can't instantiate abstract class Triangolo with abstract methods area
```
<div style="text-align: justify;">
Questo errore si presenta perchè, nella classe child <code>Triangolo</code>, non è stato implementato il metodo astratto <code>area()</code> presente nella sua classe parent. Per correggere l'errore, implementiamo questo metodo:
</div>
```
class Triangolo(Poligono):
    def __init__(self, base, altezza):
        super().__init__(tipo = 'triangolo', base = base, altezza = altezza)

    def __str__(self):
        super().__str__()
        print('Area: {0}.'.format(self.area()))

    def area(self):
        return self.base * self.altezza / 2
```
<div style="text-align: justify;">
Andando infine a rieseguire lo script:
</div>
```
try:
    triangolo = Triangolo(3,4)
except ValueError as error:
    print(error)       
else:
    triangolo.__str__()
```
<div style="text-align: justify;">
otterremo l'output:
</div>
```
Il poligono considerato è un triangolo.
Base: 3. Altezza: 4.
Area: 6.0.
```
<div style="text-align: justify;">
In conclusione, l'astrazione è uno strumento che obbliga ciascuna classe child a implementare i metodi astratti delle sue classi parent.
</div>

---
### Polimorfismo

<div style="text-align: justify;">
Il polimorfismo consiste nel definire comportamenti che sono comuni a più classi, di modo da identificare che questi posseggono, in parte, una stessa forma. Come al solito, continuiamo a sviluppare l'esempio sui poligoni. Abbiamo già introdotto la classe child <code>Triangolo</code>; allo stesso modo, possiamo introdurre la classe child <code>Rettangolo</code>, che in più possiede il metodo <code>perimetro()</code>:
</div>
```python
class Rettangolo(Poligono):
    def __init__(self, base, altezza):
        super().__init__(tipo = 'rettangolo', base = base, altezza = altezza)

    def __str__(self):
        super().__str__()
        print('Area: {0}.'.format(self.area()))

    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)
```
<div style="text-align: justify;">
A questo punto, notiamo che le classi <code>Triangolo</code> e <code>Rettangolo</code> posseggono entrambe il metodo <code>area()</code>. Possiamo allora sfruttare questa somiglianza definendo una funzione che calcoli l'area di un qualsiasi loro oggetto. Basterà infatti considerare:
</div>
```python
def calcola_area(poligono):
    return poligono.area()
```
<div style="text-align: justify;">
A questo punto, potremo calcolare indistintamente l'area di un oggetto attraverso la function suddetta, il cui input potrà essere un'istanza di <code>Triangolo</code>, di <code>Rettangolo</code> o di una qualsiasi classe che disponga di un metodo <code>area()</code>. Di conseguenza, lo script:
</div>
```python
try:
    triangolo = Triangolo(3,2)
    rettangolo = Rettangolo(4,2)
except ValueError as error:
    print(error)       
else:
    print("Area di triangolo: {0}.".format(calcola_area(triangolo)))
    print("Area di rettangolo: {0}.".format(calcola_area(rettangolo)))
```
<div style="text-align: justify;">
produrrà l'output:
</div>
```
Area di triangolo: 3.0.
Area di rettangolo: 8.
```
<div style="text-align: justify;">
Quindi il polimorfismo consente di definire funzioni che possano prendere in input oggetti di qualsiasi forma, che però posseggano un metodo in comune.
</div>

---
### Script riassuntivo

<div style="text-align: justify;">
Tutto quanto abbiamo detto nelle precedenti sottosezioni viene quindi sintetizzato in un unico script, che per completezza riportiamo qui di seguito:
</div>
```
from abc import ABC, abstractmethod

class Poligono:
    def __init__(self, tipo, base, altezza):
        self.tipo = tipo
        self.base = base
        self.altezza = altezza

    def __str__(self):
        print('Il poligono considerato è un {0}.'.format(self.tipo))
        print('Base: {0}. Altezza: {1}.'.format(self.base, self.altezza))

    @abstractmethod
    def area(self):
        pass

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        if tipo not in ('triangolo', 'rettangolo'):
            raise ValueError('[ERROR] Il tipo di poligono inserito non è supportato.')
        else:
            self._tipo = tipo
    
    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, base):
        if base <= 0:
            raise ValueError('[ERROR] La base non può essere minore o uguale a 0.')
        self._base = base

    @property
    def altezza(self):
        return self._altezza
    @altezza.setter
    def altezza(self, altezza):
        if altezza <= 0:
            raise ValueError("[ERROR] L'altezza non può essere minore o uguale a 0.")
        self._altezza = altezza

class Triangolo(Poligono):
    def __init__(self, base, altezza):
        super().__init__(tipo = 'triangolo', base = base, altezza = altezza)

    def __str__(self):
        super().__str__()
        print('Area: {0}.'.format(self.area()))

    def area(self):
        super().area()
        return self.base * self.altezza / 2

class Rettangolo(Poligono):
    def __init__(self, base, altezza):
        super().__init__(tipo = 'rettangolo', base = base, altezza = altezza)

    def __str__(self):
        super().__str__()
        print('Area: {0}.'.format(self.area()))

    def area(self):
        super().area()
        return self.base * self.altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)

def calcola_area(poligono):
    return poligono.area()

try:
    triangolo = Triangolo(3,2)
    rettangolo = Rettangolo(4,2)
except ValueError as error:
    print(error)       
else:
    print("Area di triangolo: {0}.".format(calcola_area(triangolo)))
    print("Area di rettangolo: {0}.".format(calcola_area(rettangolo)))

```




<hr>
<sup id="fn0">1. Si noti che non è necessario estendere i metodi della classe parent. Inoltre, tali metodi si possono ridefinire interamente. In tal caso si dice fare l'override del metodo.
</sup>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">