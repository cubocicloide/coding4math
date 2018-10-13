# Moduli

<div style="text-align: justify;">
In Python un modulo è essenzialmente un file che contiene del codice scritto in questo linguaggio. I moduli sono caratterizzati dall'estensione <code>.py</code>, quindi al file <code>istruzione.py</code> corrisponderà il nome modulo <code>istruzione</code>.
Lo scopo dei moduli è duplice: essi contengono istruzioni e definizioni che possono essere riutilizzate quante volte si vuole senza la necessità di doverle riscrivere, basterà importare i moduli dove necessari; inoltre, si rivelano particolarmente comodi per gestire facilmente grandi quantità di codice.
</div>

---
## Modularizzazione

<div style="text-align: justify;">
Modularizzare un software significa scomporlo in più moduli, ciascuno dei quali si occupa di svolgere uno dei compiti del programma. Per comprendere meglio, consideriamo una applicazione che si occupi di plottare l'istogramma di una lista di interi positivi, e di trovarne il valore massimo e l'indice della lista in cui viene raggiunto. Il codice che implementa il programma è scritto e commentato qui di seguito:
</div>
```
"""
Questo script ha il fine di disegnare l'istogramma di una lista di numeri interi positivi e,
al contempo, di determinare il suo valore massimo e il primo indice in cui viene raggiunto.
"""

def positive_integer(vector):
    """
    Questa funzione ha come parametro una lista, e si occupa di
    verificare che i suoi elementi siano interi positivi.
    """
    for val in vector:
        if (not isinstance(val, int)) or val <= 0:
            raise ValueError('[ERRORE] Il parametro di input deve essere composto ' + 
                             'da numeri interi positivi.')

def real_number(vector):
    """
    Questa funzione ha come parametro una lista, e si occupa di
    verificare che i suoi elementi siano numeri reali.
    """
    for val in vector:
        if not isinstance(val, (int, float)):
            raise ValueError('[ERRORE] Il parametro di input deve essere composto da numeri reali.')

def hist(vector):
    """
    Questa funzione ha come parametro una lista di numeri interi positivi,
    e serve a disegnarne il relativo istogramma sul prompt.
    """
    try:
        positive_integer(vector)
    except ValueError as error:
        print("[ERRORE] Non è possibile disegnare l'istogramma.")
        print(error)
    else:
        char = '*'
        i = 0
        for val in vector:
            print('vector[{0}]: '.format(i) + char*val)
            i = i + 1

def maximize(vector):
    """
    Questa funzione ha come parametro una lista di numeri reali,
    e serve ha trovarne il valore massimo e il primo indice cui appartiene.
    """
    try:
        real_number(vector)
    except ValueError as error:
        print("[ERRORE] Non è possibile calcolare il massimo.")
        print(error)
        [argmax, max_] = [None, None]
    else:
        argmax = 0
        max_ = 0
        i = 0
        for val in vector:
            if val > max_:
                argmax = i
                max_ = val
            i = i + 1
    return [argmax, max_]

# consideriamo una lista di interi positivi
vector = [5, 9, 3, 4]

# plottiamo l'istogramma della suddetta lista
hist(vector)

# determiniamo l'indice in cui viene raggiunto il massimo valore
# e il massimo valore della lista
[argmax, max_] = maximize(vector)

# stampiamo a video il risultato
if argmax != None and max_ != None:
    print('argmax: {0}'.format(argmax))
    print('max_: {0}'.format(max_))
```
<div style="text-align: justify;">
Eseguendo la suddetta applicazione, otterremo l'output seguente:
</div>
```
vector[0]: *****
vector[1]: *********
vector[2]: ***
vector[3]: ****
argmax: 1
max_: 9
```
<div style="text-align: justify;">
A questo punto, ci accorgiamo subito di una cosa: lo script di cui sopra si compone di un numero ragguardevole di righe di codice. Sorge quindi spontanea una domanda: è possibile scomporre lo script in più file (cioè moduli), ciascuno a sè stante? La risposta è ovviamente sì. Per prima cosa, però, occorre decidere come strutturare la nostra applicazione. Notiamo in particolare che, nel nostro esempio, vi sono:
<ul>
<li>due funzioni che si occupano di controllare gli elementi della lista, cioè <code>positive_integer</code> e <code>real_number</code>;</li>
<li>una funzione che disegna l'istogramma della lista, ovvero <code>hist</code>;</li>
<li>una funzione adibita alla ricerca del massimo della lista e dell'indice in cui viene raggiunto, detta <code>maximize</code>;</li>
<li>una porzione di codice in cui viene eseguito un test dell'intera applicazione.</li>
</ul>
Tenuto conto di ciò, si può decidere di strutturare il nostro ambiente virtuale come segue:
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
         |__validate.py
         |__plot.py
         |__optimization.py
         |__main.py
```
<div style="text-align: justify;">
dove, in particolare:
<ul>
<li>il modulo <code>validate</code> conterrà le funzioni che si occupano di validare gli elementi della lista;</li>
<li>il modulo <code>plot</code> conterrà la funzione che si occupa di disegnare l'istogramma della lista;</li>
<li>il modulo <code>optimization</code> conterrà la funzione che determina il massimo e l'argomento del massimo della lista;</li>
<li>il modulo <code>main</code> conterrà le istruzioni che verranno eseguite dall'applicazione.</li>
</ul>
Iniziamo col definire il modulo <code>validate</code>. Esso conterrà le funzioni <code>positive_integer</code> e <code>real_number</code>, e pertanto sarà dato da:
</div>
```
"""
Modulo validate: si occupa di validare gli elementi di una lista.
"""

def positive_integer(vector):
    """
    Questa funzione ha come parametro una lista, e si occupa di
    verificare che i suoi elementi siano interi positivi.
    """
    for val in vector:
        if (not isinstance(val, int)) or val <= 0:
            raise ValueError('[ERRORE] Il parametro di input deve essere composto ' + 
                             'da numeri interi positivi.')

def real_number(vector):
    """
    Questa funzione ha come parametro una lista, e si occupa di
    verificare che i suoi elementi siano numeri reali.
    """
    for val in vector:
        if not isinstance(val, (int, float)):
            raise ValueError('[ERRORE] Il parametro di input deve essere composto da numeri reali.')
```

---
## <code>import</code> statement

<div style="text-align: justify;">
Il prossimo modulo da definire è <code>plot</code>, il quale dovrà contenere la funzione <code>hist</code>. Ci accorgiamo però che questa funzione contiene una chiamata alla funzione <code>real_number</code> che adesso risiede nel modulo <code>validate</code>. Bisogna quindi fare in modo che, all'interno del modulo <code>plot</code>, sia possibile riferirsi a tale funzione. A tal fine, Python mette a disposizione l'istruzione <code>import</code>, da inserire all'inizio del modulo, che consente di importare tutti i moduli necessari alla definizione del file di interesse. In tal caso verrà usata come segue:
</div>
```
"""
Modulo plot: si occupa di disegnare gli elementi di una lista.
"""

# importiamo i moduli necessari
import validate

def hist(vector):
    """
    Questa funzione ha come parametro una lista di numeri interi positivi,
    e serve a disegnarne il relativo istogramma sul prompt.
    """
    try:
        # validiamo gli elementi della lista tramite la funzione positive_integer
        # del modulo validate importato all'inizio
        validate.positive_integer(vector) 
    except ValueError as error:
        print("[ERRORE] Non è possibile disegnare l'istogramma.")
        print(error)
    else:
        char = '*'
        i = 0
        for val in vector:
            print('vector[{0}]: '.format(i) + char*val)
            i = i + 1
```
<div style="text-align: justify;">
Si noti l'istruzione <code>import validate</code> all'inizio del file, che ci ha consentito di importare il modulo <code>validate</code>, e l'utilizzo dell'istruzione <code>validate.positive_integer(vector)</code> per effettuare una chiamata alla funzione <code>positive_integer</code> del modulo <code>validate</code>.
</div>

---
## <code>from...import</code> statement

<div style="text-align: justify;">
Osserviamo che l'istruzione <code>import</code> consente di importare tutte le funzioni e le classi presenti nel modulo importato. Questo può tradursi in un calo delle performance, specie quando ci servono solo poche funzionalità del modulo importato. Proseguendo col nostro esempio, ci accorgiamo che il modulo <code>plot</code> necessita di importare, dal modulo <code>validate</code>, la sola funzione <code>positive_integer</code>. Al fine di importare solo le funzionalità necessarie, Python mette a disposizione lo statement <code>from nome_modulo import funzione_o_classe</code>, che nel caso del modulo <code>plot</code> si traduce in quanto segue:
</div>
```
"""
Modulo plot: si occupa di disegnare gli elementi di una lista.
"""

# dal modulo validate importiamo la funzione positive_integer
from validate import positive_integer

def hist(vector):
    """
    Questa funzione ha come parametro una lista di numeri interi positivi,
    e serve a disegnarne il relativo istogramma sul prompt.
    """
    try:
        # validiamo gli elementi della lista tramite la funzione positive_integer
        # importata all'inizio
        positive_integer(vector) 
    except ValueError as error:
        print("[ERRORE] Non è possibile disegnare l'istogramma.")
        print(error)
    else:
        char = '*'
        i = 0
        for val in vector:
            print('vector[{0}]: '.format(i) + char*val)
            i = i + 1
```
<div style="text-align: justify;">
Si noti l'istruzione <code>from validate import positive_integer</code> all'inizio del file, che ci ha consentito di importare la funzione <code>positive_integer</code> dal modulo <code>validate</code>. Inoltre, a differenza dello statement <code>import</code>, la chiamata alla funzione importata non necessita della sintassi <code>validate.positive_integer(vector)</code>.<br>
&nbsp; Seguendo la stessa filosofia, definiamo il modulo <code>optimization</code>, il quale necessita, per il calcolo del massimo, della funzione <code>real_numer</code> del modulo <code>validate</code>. Pertanto tale modulo sarà così definito:
</div>
```
"""
Modulo optimization: si occupa di risolvere problemi di ottimizzazione.
"""

# dal modulo validate importiamo la funzione real_number
from validate import real_number

def maximize(vector):
    """
    Questa funzione ha come parametro una lista di numeri reali,
    e serve ha trovarne il valore massimo e il primo indice cui appartiene.
    """
    try:
        real_number(vector)
    except ValueError as error:
        print("[ERRORE] Non è possibile calcolare il massimo.")
        print(error)
        [argmax, max_] = [None, None]
    else:
        argmax = 0
        max_ = 0
        i = 0
        for val in vector:
            if val > max_:
                argmax = i
                max_ = val
            i = i + 1
    return [argmax, max_]
```

---
## <code>\__main__</code> variable

<div style="text-align: justify;">
Per terminare la modularizzazione della nostra applicazione, resta da definire il modulo <code>main</code>, che sarà il modulo da cui verrà eseguito il programma. Per la sua definizione, è buona norma introdurre una funzione <code>main()</code>, la quale verrà eseguita solo se il file <code>main.py</code> viene mandato in esecuzione dall'interprete Python. Quando ciò avviene, l'interprete assegna al fine <code>main.py</code> una variabile standard <code>__name__</code> con valore uguale a <code>"__main__"</code>. Di conseguenza, il modulo si articola come segue:
</div>
```
"""
Modulo main: è il modulo da cui viene lanciata l'applicazione.
"""

# importiamo le funzioni necessarie all'esecuzione del programma
from optimization import maximize
from plot import hist

def main():
    """
    Questa funzione contiene le istruzioni che andranno eseguite 
    quando il file main.py viene mandato in esecuzione.
    """

    # consideriamo una lista di interi positivi
    vector = [5, 9, 3, 4]

    # plottiamo l'istogramma della suddetta lista
    hist(vector)

    # determiniamo l'indice in cui viene raggiunto il massimo valore
    # e il massimo valore della lista
    [argmax, max_] = maximize(vector)

    # stampiamo a video il risultato
    if argmax != None and max_ != None:
        print('argmax: {0}'.format(argmax))
        print('max_: {0}'.format(max_))

if __name__ == '__main__':
    main()
```
<div style="text-align: justify;">
A questo punto, una volta attivato l'ambiente virtuale, potremo lanciare il <code>main.py</code> all'interno della cartella <code>src</code> come al solito:
</div>
```
(myvenv) src > python main.py
```
<div style="text-align: justify;">
e l'output prodotto sarà esattamente quello previsto:
</div>
```
vector[0]: *****
vector[1]: *********
vector[2]: ***
vector[3]: ****
argmax: 1
max_: 9
```
<div style="text-align: justify;">
Vale la pena osservare che, una volta lanciato il file <code>main.py</code>, il file system presenterà una nuova cartella, generata automaticamente dall'interprete e denominata <code>__pycache__</code>, la quale conterrà i moduli <code>validate</code>, <code>plot</code>, <code>optimization</code> (oggetto di importazione da parte del <code>main</code>) tradotti in linguaggio macchina, e che quindi avranno estensione <code>.pyc</code>. In particolare, il file system si presenterà così:
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
         |__validate.py
         |__plot.py
         |__optimization.py
         |__main.py
         |__ __pycache__
            |__validate.pyc
            |__plot.pyc
            |__optimization.pyc
```

---
## <code>as</code> keyword

<div style="text-align: justify;">
È possibile rinominare un modulo, ossia assegnargli un alias, attraverso la parola chiave <code>as</code>. Considerando ad esempio il modulo <code>validate</code>, potremmo importarlo nel modulo <code>plot</code> col nome <code>val</code>:
</div>
```
import validate as val
```
<div style="text-align: justify;">
A questo punto potremo chiamare la funzione <code>positive_integer</code> all'interno di <code>plot</code> tramite il comando
</div>
```
val.positive_integer(vector)
```

---
## Moduli standard

<div style="text-align: justify;">
Per comodità degli sviluppatori, Python prevede un gran numero di moduli standard, forniti nativamente dal linguaggio, per svolgere diversi compiti.
Questi moduli sono importabili tramite la stessa sintassi utilizzabile per i moduli definiti dagli utenti.<br>
&nbsp; Per proporre un esempio, possiamo prendere in considerazione il modulo <code>math</code> che, come suggerisce il nome, consente di gestire alcune operazioni, funzioni e costanti matematiche di base. Ad esempio, volendo stampare il numero pi-greco, basterà eseguire il seguente script
</div>
```
import math
print(math.pi)
```
<div style="text-align: justify;">
Così come i moduli definiti dagli utenti, anche i moduli standard possono essere rinominati. Nello stesso modo è possibile importare soltanto parti specifiche di un modulo, o tutte le definizioni e le istruzioni che lo compongono.
</div>



<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">