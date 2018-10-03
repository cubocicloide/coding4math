# Funzioni

<div style="text-align: justify;">
E' possibile definire le funzioni come degli insiemi composti da una o più istruzioni necessarie per lo svolgimento di un determinato compito; uno dei vantaggi derivanti dall'utilizzo di questi costrutti riguarda il fatto che essi possono essere definiti una volta sola e poi utilizzati in più di un'occasione all'interno della medesima applicazione, ciò avverrà tramite un meccanismo denominato "chiamata alla funzione".
In questo modo si eviteranno inutili ripetizioni di codice con un evidente risparmio di tempo in sede di sviluppo, a cui si accompagna la possibilità di creare sorgenti più snelli, leggibili e performanti.
Python prevede sia funzioni integrate (ad esempio, le funzioni <code>print()</code> e <code>input()</code>) che la possibilità di creare funzioni personalizzate; in questo capitolo verranno analizzate le seconde, delle prime ci occuperemo in una successiva sezione.
</div>
---
## Definire una funzione

<div style="text-align: justify;">
Si può definire una funzione adoperando la seguente, generica, sintassi:
</div>
```python
def nome_funzione(parametri):
	"""docstring"""
	blocco function
```
<div style="text-align: justify;">
In particolare, la definizione di una funzione ha le seguenti componenti:
<ul>
<li>la parola chiave <code>def</code>, che contrassegna l'inizio dell'intestazione della funzione;</li>
<li>un nome di funzione che la identifichi in modo univoco;</li>
<li>parametri o argomenti (opzionali) attraverso i quali passiamo valori alla funzione;</li>
<li>due punti <code>:</code> per contrassegnare la fine dell'intestazione della funzione;</li>
<li>stringa di documentazione facoltativa, detta <code>docstring</code>, per descrivere cosa fa la funzione;</li>
<li>un blocco di codice che contiene le istruzioni che saranno eseguite dalla funzione;</li>
<li>un'istruzione di <code>return</code> (opzionale e che vedremo in seguito) che consente alla funzione di restituire un valore.</li>
</ul>
Per utilizzare una funzione è richiesta una chiamata esplicita ad essa in un qualsiasi punto del codice, tale operazione potrà essere effettuata invocando il nome della funzione e passando ad essa i parametri eventualmente richiesti sotto forma di valori o di variabili:
</div>
```python
nome_funzione(eventuali_parametri)
```
---
## Docstring

<div style="text-align: justify;">
La prima stringa dopo l'intestazione della funzione è chiamata <code>docstring</code> ed è l'abbreviazione di <i>documentation string</i>. Tale stringa è utilizzata per spiegare, in breve, quello che fa la funzione.<br>

&nbsp; Sebbene facoltativa, l'inserimento di una <code>docstring</code> è una buona pratica di programmazione, che consente allo sviluppatore e agli utilizzatori del programma di comprendere meglio la logica della funzione. Si consideri, a titolo di esempio, il seguente codice:
</div>
```python
def lavori_in_corso():
    """
    In questa funzione implementeremo una delle
    richieste del nostro cliente, per il momento 
    non ancora nota.
    """
    pass

print(lavori_in_corso.__doc__)
```
<div style="text-align: justify;">
Ebbene, in questo esempio stiamo supponendo che il nostro cliente voglia sviluppare una certa funzione, non ancora nota, che codificheremo in seguito (da qui l'utilizzo della già nota keyword <code>pass</code>). Eseguendo lo script, otterremo il seguente messaggio, contenente la descrizione della funzione:
</div>
```python
In questa funzione implementeremo una delle
richieste del nostro cliente, per il momento 
non ancora nota.
```
---
## Arguments
<div style="text-align: justify;">
Come preannunciato, possiamo passare dei parametri di input alle funzioni. Questi ultimi svolgono sostanzialmente la funzione di placeholders (<i>segnalibri</i>), comunicando all'applicazione il numero di argomenti che dovranno essere passati alla funzione; questi ultimi potranno essere valorizzati arbitrariamente dallo sviluppatore sulla base delle proprie esigenze.
A questo proposito, la funzione presentata nell'esempio seguente ha il compito di concatenare tre parametri (<code>nome</code>, <code>cognome</code> e <code>msg</code>) restituendoli in output all'interno di un stringa:
</div>
```python
def saluto(nome, cognome, msg):
    """
    La funzione genera stampa sul prompt 
    una stringa prodotta dalla concatenazione 
    dei valori dei parametri passati ad essa.
    """
    print("Salve, " + nome + " " + cognome + ". " + msg)

# chiamata alla funzione
saluto("Franco", "Rossi", "Come stai?")
```
<div style="text-align: justify;">
Il risultato dell'esecuzione del codice proposto e della chiamata alla funzione <code>saluto</code> sarà il seguente:
</div>
```python
Salve, Franco Rossi. Come stai?
```
---
### Default arguments
<div style="text-align: justify;">
Python consente anche la definizione di parametri di default attraverso l'operatore di assegnamento <code>=</code>. Qui un esempio in cui al parametro <code>msg</code> viene assegnato il valore di default <code>"Come stai?"</code>:
</div>
```python
def saluto(nome, cognome, msg = "Come stai?"):
    """
    La funzione genera stampa sul prompt 
    una stringa prodotta dalla concatenazione 
    dei valori dei parametri passati ad essa.
    """
    print("Salve, " + nome + " " + cognome + ". " + msg)

# chiamata alla funzione
saluto("Franco", "Rossi")
saluto("Andrea", "Bianchi", "Erano settimane che non ci incontravamo.")
```
<div style="text-align: justify;">
Il relativo output sarà:
</div>
```python
Salve, Franco Rossi. Come stai?
Salve, Andrea Bianchi. Erano settimane che non ci incontravamo.
```
<div style="text-align: justify;">
Si noti che, quando nella chiamata alla funzione non viene specificato il parametro <code>msg</code>, allora quest'ultimo assume il suo valore di default.<br>

&nbsp; A livello di sintassi, il linguaggio Python non consente di definire i parametri di default prima di quelli non di default. Infatti, l'intestazione:
</div>
```python
def saluto(msg = "Come stai?", nome, cognome):
```
<div style="text-align: justify;">
produrrà il seguente errore:
</div>
```python
SyntaxError: non-default argument follows default argument
```
---
### Keyword arguments
<div style="text-align: justify;">
Quando chiamiamo una funzione con alcuni valori, questi valori vengono assegnati agli argomenti in base alla loro posizione.

Ad esempio, riferendoci alla funzione <code>saluto()</code>, durante la chiamata <code>saluto("Andrea", "Bianchi", "Come stai?")</code>, il valore <code>Andrea</code> viene assegnato al parametro <code>nome</code>, <code>Bianchi</code> al parametro <code>cognome</code>, e infine <code>Come stai?</code> al parametro <code>msg</code>.<br>

&nbsp; Python consente di chiamare le funzioni usando anche le keyword dei parametri. Quando chiamiamo le funzioni in questo modo, l'ordine dei parametri può essere modificato. Le chiamate successive sono infatti tutte valide, e producono lo stesso risultato.
</div>
```python
saluto(nome = "Andrea", cognome = "Bianchi", msg = "Come stai?")
saluto(cognome = "Bianchi", nome = "Andrea", msg = "Come stai?")
saluto(msg = "Come stai?", cognome = "Bianchi", nome = "Andrea")
```
<div style="text-align: justify;">
Occorre tuttavia evitare di mixare i due metodi, cioè assegnare alcuni valori tramite posizione, e altri tramite keyword. Infatti, la chiamata:
</div>
```python
saluto(nome = "Andrea", "Bianchi", "Come stai?")
```
<div style="text-align: justify;">
produrrà l'errore:
</div>
```python
SyntaxError: non-keyword arg after keyword arg
```
---
### Arbitrary arguments

<div style="text-align: justify;">
A volte, non conosciamo in anticipo il numero di argomenti che saranno passati in una funzione. Tuttavia, Python ci permette di gestire questo tipo di situazione attraverso chiamate di funzioni con un numero arbitrario di argomenti.
In tal caso, nella definizione della funzione, basterà utilizzare l'asterisco <code>*</code> prima del nome per indicare un parametro composto da un numero indefinito di argomenti. Ecco un esempio.
</div>
```python
def ciao(*args):
   """
   Questa funzione saluta tutte le persone contenute 
   nella tupla args.
   """

   for arg in args:
       print("Ciao ", arg)

ciao("Monica","Grazia","Luigi","Giovanni")
```
<div style="text-align: justify;">
Il relativo output sarà:
</div>
```python
Ciao Monica
Ciao Grazia
Ciao Luigi
Ciao Giovanni
```
<div style="text-align: justify;">
Analogamente, può capitare di dover passare alla funzione un numero indefinito di keyword arguments. In tal caso, si potrà ricorrere al doppio asterisco <code>**</code> prima del nome per indicare un parametro composto da un numero indefinito di keyword arguments. Qui un esempio:
</div>
```python
def portate(**kwargs):
    """
    Questa funzione elenca le portate
    previste nel menu.
    """

    for key in kwargs:
        value = kwargs[key]
        print(key + ": " + value)

portate(antipasto = "mozzarelle", primo = "carbonara", secondo = "bistecca", dolce = "budino")
```
<div style="text-align: justify;">
L'output prodotto sarà:
</div>
```python
antipasto: mozzarelle
primo: carbonara
secondo: bistecca
dolce: budino
```
---
## Return
<div style="text-align: justify;">
Esistono anche funzioni che restituiscono dei valori. In tal caso, il valore restituito seguirà l'istruzione <code>return</code>, la quale chiude di fatto il blocco della funzione stessa. Qualora l'istruzione <code>return</code> sia assente, il valore restituito sarà invece uguale a <code>None</code>. Qui di seguito proponiamo una funzione che restituisce il valore assoluto di un numero:
</div>
```python
def valore_assoluto(num):
	"""
    Questa funzione restituisce il valore assoluto
    del numero inserito in ingresso.
    """

	if num >= 0:
		return num
	else:
		return -num

# Output: 2
print(valore_assoluto(2))

# Output: 4
print(valore_assoluto(-4))
```

---
## Scope e ciclo di vita

<div style="text-align: justify;">
Lo scope (o visibilità) di una variabile è la parte di un programma in cui la variabile è riconosciuta. I parametri e le variabili definiti all'interno di una funzione non sono visibili dall'esterno. Quindi, hanno uno scope locale.<br>

&nbsp; Il ciclo di vita di una variabile è invece il periodo attraverso il quale la variabile viene inserita e poi cancellata dalla memoria. Il ciclo di vita delle variabili all'interno di una funzione è pari al tempo necessario all'esecuzione della funzione stessa.

Tali variabili sono distrutte una volta che la funzione termina, ragion per cui una funzione non ricorda i valori assunti dalle sue variabili locali nelle chiamate precedenti.

Ecco un esempio per illustrare lo scope e il ciclo di vita di una variabile all'interno di una funzione.
</div>
```python
def my_func():
	x = 10
	print("Il valore di x nella funzione è: ", x)

x = 20
my_func()
print("Il valore di x fuori dalla funzione è: ", x)
```
<div style="text-align: justify;">
L'output del programma sarà:
</div>
```python
Il valore di x nella funzione è: 10
Il valore di x fuori dalla funzione è: 20
```
<div style="text-align: justify;">
Possiamo vedere che il valore di <code>x</code> è inizialmente <code>20</code>. Anche se la funzione <code>my_func()</code> ha cambiato il valore di <code>x</code> a <code>10</code>, non ha influenzato il suo valore al di fuori della funzione.

Questo perché la variabile <code>x</code> all'interno della funzione è diversa da quella all'esterno. Sebbene abbiano lo stesso nome, sono due variabili differenti con scope differenti.

D'altra parte, le variabili esterne alla funzione sono visibili dall'interno, vale a dire che hanno uno scope globale.

Possiamo leggere questi valori dall'interno della funzione ma, badate bene, non possiamo modificarli. Affinché una funzione sia in grado di modificare il valore delle variabili al di fuori di essa, tali variabili devono essere dichiarate come globali utilizzando la parola chiave <code>global</code>. Infatti, eseguendo lo script:
</div>
```python
def my_func():
    global x
	x = 10
	print("Il valore di x nella funzione è: ", x)

x = 20
my_func()
print("Il valore di x fuori dalla funzione è: ", x)
```
<div style="text-align: justify;">
otterremo l'ouput:
</div>
```python
Il valore di x nella funzione è: 10
Il valore di x fuori dalla funzione è: 10
```

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">