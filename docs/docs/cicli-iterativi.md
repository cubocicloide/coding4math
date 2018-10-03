# Cicli iterativi

<div style="text-align: justify;">
I cicli iterativi sono largamente utilizzati in programmazione, e consistono nell'esecuzione di uno stesso insieme di istruzioni fintanto che una certa condizione viene verificata. Nel seguito, esamineremo i due principali cicli iterativi messi a disposizione dal linguaggio Python, ossia il ciclo <code>for</code> e il ciclo <code>while</code>.
</div>

---
## Ciclo <code>for</code>

<div style="text-align: justify;">
Il ciclo (anche detto loop) <code>for</code> è un costrutto che consente di ripetere una data operazione su ciascun elemento di una sequenza (che potrà essere, ad esempio, una stringa, una lista, una tupla o un dizionario). La sintassi prevista per l'utilizzo del ciclo <code>for</code> è:
</div>
```python
for val in sequence:
    blocco for
```
<div style="text-align: justify;">
dove <code>val</code> è la variabile che prende, ad ogni iterazione, il valore di ciascun elemento della sequenza <code>sequence</code>. Il seguente diagramma di flusso sintetizza la logica del ciclo <code>for</code> nel caso in cui si consideri la sequenza <code>sequence = range(n)</code> (ovvero, si ha che <code>sequence</code> è la lista dei primi <code>n</code> numeri interi, da <code>0</code> a <code>n - 1</code>):
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/for.svg" style="width: 250px;"><br><br>
A titolo di esempio, possiamo considerare il seguente script:
</div>
```python
"""
In questo programma calcoliamo la somma di 
tutti i numeri contenuti in una data lista.
"""

# lista di numeri
numeri = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# inizializziamo la variable che conterrà la somma
somma = 0

# iteriamo sugli elementi della lista
for val in numeri:
	somma = somma + val

# output: La somma è 48
print("La somma è ", somma)
```
<div style="text-align: justify;">
quando tale programma sarà eseguito, restituirà l'output:
</div>
```python
La somma è 48
```
<div style="text-align: justify;">
In precedenza, abbiamo fatto cenno alla funzione <code>range()</code>. Tale funzione può essere usata per generare una sequenza di numeri interi; ad esempio, <code>range(10)</code> genererà la sequenza dei primi <code>10</code> numeri interi, cioè da <code>0</code> a <code>9</code>.

Possiamo usare la funzione <code>range()</code> in un <code>for</code> loop per scorrere una sequenza di indici. Infatti, possiamo utilizzarla in combinazione con la funzione <code>len()</code> (che fornisce la lunghezza della sequenza) per iterare attraverso l'indicizzazione. Ecco un esempio:
</div>
```python
"""
In questo programma iteriamo su di una lista
attraverso l'indicizzazione dei suoi elementi.
"""

genere = ['pop', 'rock', 'jazz']

for i in range(len(genere)):
	print("Mi piace il ", genere[i])
```
<div style="text-align: justify;">
Eseguendo il suddetto script, otterremo l'output:
</div>
```python
Mi piace il pop
Mi piace il rock
Mi piace il jazz
```

---
## Ciclo <code>while</code>

<div style="text-align: justify;">
Il ciclo <code>while</code> si differenzia dal ciclo <code>for</code> precedentemente descritto più a livello sintattico che funzionale; in generale è comunque possibile affermare che mentre nel ciclo <code>for</code> le iterazioni proseguono fino al raggiungimento dell'ultimo elemento della sequenza iterata, nel ciclo <code>while</code> le iterazioni continuano finché la condizione di test passata come argomento rimane vera. La sintassi prevista per l'utilizzo del ciclo <code>while</code> è:
</div>
```python
while condizione:
	blocco while
```
<div style="text-align: justify;">
Nel ciclo <code>while</code>, l'espressione test, denominata in tal caso <code>condizione</code>, viene controllata per prima. Si eseguirà poi il <code>blocco while</code> solo se la <code>condizione</code> è vera. Dopo un'iterazione, l'espressione di test viene ricontrollata. Questo processo continua fino a quando la <code>condizione</code> diventa falsa. Di seguito proponiamo il diagramma di flusso che sintetizza quanto appena esposto:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/while.svg" style="width: 250px;"><br><br>
A titolo di esempio, consideriamo il seguente script:
</div>
```python
"""
In questo programma calcoliamo la somma dei primi n numeri interi:
somma = 1 + 2 + 3 + ... + n
"""

# Per prelevare l'input dall'utente, utilizzare l'istruzione:
# n = int(input("Inserire n: "))

n = 10

# inizializziamo la somma e il contatore
somma = 0
i = 1

while i <= n:
    somma = somma + i
    i = i + 1    # aggiorna il contatore

# stampa la somma
print("La somma è ", sum)
```
<div style="text-align: justify;">
Eseguendo il suddetto codice, l'output sarà:
</div>
```python
La somma è 55
```
<div style="text-align: justify;">
Nel programma precedente, l'espressione di test sarà vera finché la nostra variabile contatore <code>i</code> risulterà minore o uguale a <code>n</code> (<code>10</code>, nel nostro esempio).

Si noti che abbiamo bisogno di aumentare il valore della variabile contatore all'interno del blocco <code>while</code>. In caso contrario, infatti, si otterrà un loop infinito, in quanto il programma non riuscirà mai a considerare falsa l'espressione di test.
</div>

---
## Istruzione <code>break</code>

<div style="text-align: justify;">
L'istruzione <code>break</code>, quando impiegata all'interno di un ciclo iterativo, si occuperà di terminarlo in corrispondenza di un determinato evento, come per esempio il verificarsi di una condizione specifica.
Sostanzialmente <code>break</code> rappresenta uno strumento attraverso il quale influenzare il flusso di esecuzione di un ciclo e, più in generale, di un'applicazione.<br>

&nbsp; Data la sua natura, è logico dedurre che <code>break</code> sia stato concepito per essere impiegato in associazione a condizioni introdotte tramite <code>if</code>, e di fatto la sua sintassi, nel caso di ciclo <code>for</code> (ma funziona analogamente col ciclo <code>while</code>) è la seguente:
</div>
```python
for val in sequence:
	blocco istruzioni_1
	if condizione:
		break
	blocco istruzioni_2
```
<div style="text-align: justify;">
In questo caso, il programma uscirà immediatamente dal loop non appena la <code>condizione</code> viene valutata vera, senza perciò dover iterare su tutti gli elementi di <code>sequence</code>. Il diagramma di flusso seguente sintetizza quanto appena detto:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/break.svg" style="width: 300px;"><br>
A titolo di esempio, è possibile analizzare lo script seguente, che riassume in poche righe il ruolo di <code>break</code> nella terminazione di un ciclo iterativo, nel caso in cui la condizione definita tramite <code>if</code> risulti vera:
</div>
```python
"""
Uso dell'istruzione break per terminare un ciclo 
al verificarsi di una condizione introdotta con if.
"""

for val in "python":
    if val == "h":
        break
    print(val)

print("Basta così.")
```
<div style="text-align: justify;">
Eseguendo la piccola applicazione appena proposta si otterrà in output un risultato simile a quello mostrato di seguito:
</div>
```
p
y
t
Basta così.
```
<div style="text-align: justify;">
In pratica il <code>for</code> dovrà occuparsi di ciclare la stringa passata come argomento (<code>"python"</code>) stampando uno per uno i caratteri che la compongono; teoricamente il loop applicato su tale sequenza dovrebbe dare luogo a sei iterazioni, tante quanti sono i caratteri che compongono la stringa, ma la condizione introdotta da <code>if</code> richiede che venga verificata l'identità tra il carattere iterato e <code>"h"</code>; se questa condizione dovesse essere soddisfatta allora break bloccherà l'esecuzione del ciclo impedendo ulteriori iterazioni, e verrà stampata la notifica prevista per questo caso (<code>Basta così.</code>).
Grazie all'istruzione di terminazione inserita in un costrutto condizionale avremo quindi soltanto tre iterazioni più un messaggio da parte dell'applicazione.
</div>

---
## Istruzione <code>continue</code>

<div style="text-align: justify;">
Come già sottolineato, <code>break</code> risulta particolarmente utile quando si ha l'esigenza di terminare un ciclo in corrispondenza di una condizione precedentemente definita; in alcuni casi però lo sviluppatore potrebbe non necessitare di un arresto completo del loop, e voler semplicemente evitare che quest'ultimo produca delle specifiche iterazioni. A questo scopo è disponibile un'ulteriore istruzione denominata <code>continue</code>: essa in pratica arresta l'iterazione che soddisfa una determinata condizione, ma permette il proseguimento del ciclo nella quale viene impiegata. La sua sintassi, nel caso di ciclo <code>for</code> (ma funziona analogamente col ciclo <code>while</code>), risulterà essere:
</div>
```python
for val in sequence:
	blocco istruzioni_1
	if condizione:
		continue
	blocco istruzioni_2
```
<div style="text-align: justify;">
Esaminando più nel dettaglio la suddetta sintassi, avremo che, per ogni iterazione sugli elementi di <code>sequence</code>, il <code>blocco istruzioni_1</code> sarà sempre eseguito. Tuttavia, il <code>blocco istruzioni_2</code> sarà eseguito solo per quegli elementi di <code>sequence</code> che non verificano il test <code>condizione</code>. Di seguito proponiamo il diagramma di flusso che sintetizza quanto appena detto:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/continue.svg" style="width: 300px;"><br>
Per chiarire meglio l'utilizzo dell'istruzione <code>continue</code>, proponiamo infine una variante dello script esaminato nella precedente sottosezione:
</div>
```python
"""
Uso dell'istruzione continue per arrestare un'iterazione
al verificarsi di una condizione introdotta con if
"""

for val in "python":
    if val == "h":
        continue
    print(val)

print("Ciclo completato.")
```
<div style="text-align: justify;">
Una volta eseguita l'applicazione appena digitata si otterrà in output un risultato come quello presentato di seguito:
</div>
```
p
y
t
o
n
Ciclo completato.
```
<div style="text-align: justify;">
Anche in questo caso <code>for</code> avrà il compito di ciclare una stringa, stampando in output, uno alla volta, tutti i caratteri da cui è composta; ciò però non avverrà se non in parte, perché <code>if</code> introduce una condizione di identità: nel momento in cui il carattere iterato dovesse essere uguale ad <code>"h"</code>, questo verrà ignorato e non parteciperà al risultato del ciclo; il loop non verrà però interrotto, nel senso che verranno effettuate tutte le iterazioni successive previste.
</div>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">