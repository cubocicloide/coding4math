# Costrutti condizionali

<div style="text-align: justify;">
Come la maggior parte dei linguaggi di programmazione, anche Python mette a disposizione i cosiddetti costrutti condizionali; in sostanza parliamo di espressioni il cui esito, cioè il risultato prodotto, dipende dalla verifica o meno di una condizione precedentemente definita. Per la definizione di un costrutto condizionale si utilizzano le keywords <code>if</code> (l'unica obbligatoria), <code>elif</code> ed <code>else</code>, gli esempi proposti di seguito ne evidenzieranno il funzionamento.
</div>

---
## <code>if</code> statement

<div style="text-align: justify;">
La keyword <code>if</code> ha il compito di introdurre una condizione che, se viene verificata, comporterà l'esecuzione di un blocco di codice dedicato. In caso contrario, tale blocco sarà ignorato. Sintatticamente, un <code>if</code> statement, in Python, ha la seguente forma:
</div>
```python
if condizione:
    istruzione
```
<div style="text-align: justify;">
In questo caso, il programma valuta la <code>condizione</code>, ed esegue l'<code>istruzione</code> solo se la <code>condizione</code> è <code>True</code>. Dunque, se la <code>condizione</code> è <code>False</code>, l'<code>istruzione</code> non viene eseguita. Si noti, in particolare, che in Python il blocco dell'<code>if</code> statement viene preceduto dai due punti <code>:</code>, ed è indicato dal suo livello di indentazione. Infatti, il corpo dell'<code>if</code> comincia con un nuovo livello di indentazione, e termina quando questo nuovo livello di indentazione viene rimosso.<br>
&nbsp; Altra cosa da ricordare, quando si utilizza un <code>if</code> statement, è la seguente: Python interpreta come <code>True</code> tutti i valori non nulli e diversi da zero. Gli unici valori considerati come <code>False</code> sono quindi <code>None</code> (ossia, il valore nullo) e <code>0</code>. Detto questo, riportiamo di seguito il diagramma di flusso dell'<code>if</code> statement, che sintetizza quanto detto in precedenza.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/if.svg" style="width: 250px;"><br>

Concludiamo questa sottosezione dedicata all'<code>if</code> statement con un semplice esempio:
</div>
```python
# se il numero è positivo, stampa un messaggio appropriato
num = 3
if num > 0:
    print(num + "è un numero positivo.")
print("Questo messaggio viene sempre stampato.")

num = -1
if num > 0:
    print(num + "è un numero positivo.")
print("Anche questo messaggio viene sempre stampato.")
```

<div style="text-align: justify;">
Quando questo programma viene eseguito, l'output risulterà essere:
</div>
```python
3 è un numero positivo.
Questo messaggio viene sempre stampato.
Anche questo messaggio viene sempre stampato.
```

<div style="text-align: justify;">
Come possiamo osservare, nell'esempio precedente <code>num > 0</code> è la condizione che stiamo valutando. Il blocco dell'<code>if</code> viene eseguito solo quando tale condizione è <code>True</code>. In particolare, quando la variabile <code>num</code> è uguale a <code>3</code>, allora la condizione è vera e il blocco dell'<code>if</code> viene eseguito. Quando invece la variabile <code>num</code> è pari a <code>-1</code>, il blocco dell'<code>if</code> viene saltato. Inoltre, le istruzioni di <code>print()</code> che sono al di fuori dei blocchi <code>if</code> verranno sempre eseguite, indipendentemente dal risultato della verifica.
</div>

------
## <code>if...else</code> statement

<div style="text-align: justify;">
Nei costrutti condizionali, la keyword <code>else</code> consente di definire un'istruzione alternativa che verrà eseguita quando una condizione imposta tramite <code>if</code> non dovesse verificarsi. Sintatticamente, un <code>if...else</code> statement, in Python, ha la seguente forma:
</div>
```python
if condizione:
    blocco dell'if
else:
    blocco dell'else
```

<div style="text-align: justify;">
Ebbene, l'<code>if...else</code> statement valuta la <code>condizione</code> ed esegue il <code>blocco dell'if</code> solo se la <code>condizione</code> è <code>True</code>. Se invece la <code>condizione</code> è <code>False</code>, viene invece eseguito il <code>blocco dell'else</code>. Anche in tal caso l'indentazione è usata per separare i due blocchi. Detto questo, riportiamo di seguito il diagramma di flusso dell'<code>if...else</code> statement, che sintetizza quanto detto in precedenza.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/if-else.svg" style="width: 330px;"><br>
Concludiamo questa sottosezione dedicata all'<code>if...else</code> statement con un semplice esempio:
</div>
```python
# Il programma verifica se il numero è positivo o negativo,
# per poi mostrare un messaggio appropriato
num = 3

# Per testare il programma, si provi a utilizzare anche i seguenti valori di num: 
# num = -5
# num = 0

if num >= 0:
    print("Numero maggiore o uguale a zero.")
else:
    print("Numero negativo")
```

<div style="text-align: justify;">
Nel suddetto esempio, quando <code>num</code> è uguale a <code>3</code>, la condizione viene verificata, di conseguenza il blocco dell'<code>if</code> viene eseguito mentre quello dell'<code>else</code> viene ignorato.<br>
&nbsp; Se invece <code>num</code> è uguale a <code>-5</code>, la condizione non viene verificata, e stavolta il blocco dell'<code>if</code> viene ignorato mentre quello dell'<code>else</code> viene eseguito.<br>
&nbsp; Infine, se <code>num</code> è pari a <code>0</code>, la condizione è vera e quindi, come nel primo caso, il blocco dell'<code>if</code> viene eseguito mentre quello dell'<code>else</code> viene saltato.
</div>

------
## <code>if...elif...else</code> statement

<div style="text-align: justify;">
La keyword <code>elif</code> è un diminutivo per <i>else if</i>. Si tratta di una parola chiave che consente verifiche di più condizioni. In particolare, se la condizione dell'<code>if</code> è <code>False</code>, allora si passa alla verifica della condizione del successivo blocco <code>elif</code>, e così via. Infine, se tutte le condizioni incontrate lungo il cammino sono <code>False</code>, allora viene eseguito il blocco dell'<code>else</code>. Si noti che solo un blocco, tra i vari blocchi <code>if...elif...else</code>, viene eseguito. Inoltre, ciascun blocco <code>if</code> può essere associato a più blocchi <code>elif</code>, ma può avere un unico blocco <code>else</code>. Detto questo, riportiamo di seguito il diagramma di flusso dell'<code>if...elif...else</code> statement, che sintetizza quanto detto in precedenza.
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/if-elif-else.svg" style="width: 490px;"><br>
Concludiamo questa sottosezione dedicata all'<code>if...elif...else</code> statement con un semplice esempio:
</div>
```python
# In questo programma, verifichiamo se il numero
# è positivo, uguale a zero, o negativo, per
# poi stampare un messaggio adeguato
num = 3.4

# Per testare il programma, si provi a utilizzare anche i seguenti valori di num
# num = 0
# num = -4.5

if num > 0:
    print("Numero positivo")
elif num == 0:
    print("Numero uguale a zero")
else:
    print("Numero negativo")
```

<div style="text-align: justify;">
Commentiamo il suddetto script: quando la variabile <code>num</code> è positiva, il programma stampa il messaggio <code>Numero positivo</code>. Se invece <code>num</code> è uguale a <code>0</code>, viene stampato <code>Numero uguale a zero</code>. Infine, se nessuna delle condizioni precedenti è verificata, sul display apparirà la scritta <code>Numero negativo</code>.
</div>

------
## <code>if</code> statement annidati

<div style="text-align: justify;">
Possiamo avere casi in cui un <code>if...elif...else</code> statement è all'interno di un altro <code>if...elif...else</code> statement. In linguaggio informatico questa situazione viene indicata come un annidamento di strutture. Ovviamente, possiamo iterare il ragionamento, nel senso che possiamo considerare un <code>if...elif...else</code> statement all'interno di un altro <code>if...elif...else</code> statement che è a sua volta dentro un terzo <code>if...elif...else</code> statement. L'unico modo che abbiamo per capire in quale di questi statement ci troviamo è un attenta lettura dei livelli di indentazione. Val la pena notare che le strutture annidate possono creare confusione e, quindi, vanno usate con cautela.<br>
&nbsp; Concludiamo questa sottosezione con un esempio:
</div>
```python
# In questo programma, l'utente inserisce in input un numero. 
# Tale numero viene poi sottoposto a verifiche annidate per
# capire se è positivo, negativo oppure se è uguale a zero.
# Infine, viene stampato un messaggio appropriato.
num = float(input("Inserire un numero: "))

if num >= 0:
    if num == 0:
        print("Numero uguale a zero")
    else:
        print("Numero positivo")
else:
    print("Numero negativo")
```
<div style="text-align: justify;">
Si lascia al lettore, come esercizio, la verifica dell'output prodotto dal programma nelle diverse situazioni.
</div>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">