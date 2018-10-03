# Input/Output

<div style="text-align: justify;">
Python fornisce numerose funzioni integrate che ci consentono di interfacciarci con il prompt.

Alcune di queste funzioni, come ad esempio <code>input()</code> e <code>print()</code>, sono ampiamente utilizzate, rispettivamente, per le operazioni standard di input e output. Incominciamo a vedere per prima la sezione dedicata agli output.
</div>

---
## Output mediante <code>print()</code>

<div style="text-align: justify;">
Come abbiamo già avuto modo di vedere nelle precedenti sezioni, possiamo usare la funzione <code>print()</code> per stampare i dati sul prompt. Un esempio del suo utilizzo è dato qui sotto:
</div>
```python
print('questa frase viene stampata sullo schermo')
# output: questa frase viene stampata sullo schermo

a = 5
print('il valore di a è', a)
# output: il valore di a è 5
```
<div style="text-align: justify;">
La sintassi della funzione <code>print()</code> è
</div>
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
<div style="text-align: justify;">
Si noti in particolare che:
<ul>
<li><code>objects</code> sono gli oggetti che verranno stampati;</li>
<li><code>sep</code> è il separatore che sarà utilizzato tra i diversi oggetti (il suo valore di default è il carattere spazio);</li>
<li><code>end</code> è ciò che viene stampato subito dopo gli oggetti (il suo valore di default è <code>\n</code>, che corrisponde all'andata a capo);</li>
<li><code>file</code> indica dove l'oggetto sarà stampato (il suo valore di default è <code>sys.stdout</code>, ovvero il prompt di Python).</li>
</ul>
Di seguito forniamo un esempio in cui variamo alcuni dei valori di default:
</div>
```python
print(1,2,3,4)
# output: 1 2 3 4

print(1,2,3,4,sep='*')
# output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# output: 1#2#3#4&
```
<div style="text-align: justify;">
A volte vorremmo formattare il nostro output per renderlo più elegante. Ciò può essere fatto usando il metodo <code>str.format()</code>. Questo metodo può essere applicato a qualsiasi oggetto stringa. Nell'esempio seguente, le parentesi graffe <code>{}</code> sono usate come segnaposti per l'inserimento degli oggetti da stampare; possiamo inoltre specificare l'ordine di stampa indicizzando le parentesi stesse, o addirittura utilizzare delle keyword come argomenti al loro interno:
</div>
```python
print('ordine di arrivo: {0}, {1}'.format('vettel','raikkonen'))
# output: ordine di arrivo: vettel, raikkonen

print('ordine di arrivo: {1}, {0}'.format('vettel','raikkonen'))
# output: ordine di arrivo: raikkonen, vettel

print('mi chiamo {nome} {cognome}'.format(nome='franco',cognome='rossi'))
# output: mi chiamo franco rossi
```

---
## Input mediante <code>input()</code>

<div style="text-align: justify;">
Fino ad ora, i nostri programmi sono stati statici, nel senso che il valore delle variabili è stato definito o codificato nel codice sorgente.

Per consentire flessibilità, potremmo voler prendere l'input dell'utente. In Python, abbiamo la funzione <code>input()</code> a tal fine. La sintassi per <code>input()</code> è:
</div>
```python
input([prompt])
```
<div style="text-align: justify;">
dove <code>prompt</code> è la stringa (opzionale) che vogliamo mostrare sullo schermo. Val la pena osservare che qualsiasi valore fornito in ingresso dall'utente tramite la funzione <code>input()</code> sarà un oggetto stringa e che, quindi, potrà esserci il bisogno di convertire l'input nel formato desiderato:
</div>
```python
num = input('inserire un numero intero: ')
# >>> inserire un numero intero: 
# >>> 10 
# l'utente ha inserito il numero 10, ma num è in realtà la stringa '10';
# la convertiamo perciò in un intero:
num = int(num)  
```



<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">