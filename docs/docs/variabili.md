# Variabili

<div style="text-align: justify;">
Le variabili non sono altro che locazioni di memoria in cui è possibile immagazzinare dei dati. Ciò significa che quando si crea una variabile, viene riservata una cella memoria. In base al tipo di una variabile, l'interprete decide poi cosa potrà essere memorizzato in essa. All'interno di una variabile, in funzione dei diversi tipi di dati, sarà quindi possibile memorizzare, ad esempio, numeri interi, decimali o caratteri.
</div>

------
## Assegnare valori alle variabili

<div style="text-align: justify;">
Una variabile Python non ha bisogno di una dichiarazione esplicita affinché le venga riservata una locazione di memoria. Infatti, la dichiarazione avviene automaticamente quando, alla variabile, viene assegnato un valore.<br>

&nbsp; Per assegnare un valore a una variabile viene utilizzato il segno di uguaglianza (<code>=</code>). L'operando alla sinistra di <code>=</code> sarà il nome della variabile, mentre l'operando a destra di <code>=</code> sarà il valore memorizzato nella variabile. Ad esempio:
</div>
```python
counter = 100          # numero intero
miles   = 1000.1       # floating point
name    = "John"       # stringa

print(counter)
print(miles)
print(name)
```
<div style="text-align: justify;">
In questo caso, abbiamo che 100, 1000.1 e "John" sono i valori assegnati alle variabili <i>counter</i>, <i>miles</i> e <i>name</i>. Il suddetto script produrrà il risultato seguente:
</div>

```zsh
100
1000.1
John
```

------
## Tipi di dati standard

<div style="text-align: justify;">
I dati in memoria possono essere di diversi tipi. Per esempio, l'età di una persona viene immagazzinata come un numero intero, mentre il suo indirizzo è memorizzato tramite caratteri alfanumerici. Python possiede una varietà di tipi di dati standard, per i quali sono state definite operazioni e metodi che su essi possono essere utilizzati. Nello specifico, esistono 5 tipi di dati standard:
<ul>
<li>Numeri</li>
<li>Stringhe</li>
<li>Liste</li>
<li>Tuple</li>
<li>Dizionari</li>
</ul>
</div>

------
## Numeri

<div style="text-align: justify;">
I tipi di dati numerici vengono creati quando si assegna loro un valore numerico, ad esempio:
</div>
```python
var_1 = 1
var_2 = 10
```
<div style="text-align: justify;">
Python supporta quattro diversi tipi di dati numerici:
<ul>
<li><code>int</code>: numeri interi con segno (i.e., positivi o negativi)</li>
<li><code>float</code>: numeri con virgola mobile (e.g., numeri razionali o reali)</li>
<li><code>complex</code>: numeri complessi</li>
<li><code>long</code>: numeri interi lunghi (possono anche essere espressi in base ottale o esadecimale)</li>
</ul>
Di seguito proponiamo alcuni esempi delle sopra elencate tipologie di numeri:
</div>

| **int** | **float** | **complex** | **long** |
| -- | -- | -- | -- |
| 10 | 0.0 | 3.14j | 51924361L |
| 100 | 15.20 | 45.j | -0x19323L |
| -786 | -21.9 | 9.322e-36j | 0122L |
| 080 | 32.3+e18 | .876j | 0xDEFABCECBDAECBFBAEl |
| -0490 | -90 | -.6545+0J | 535633629843L |
| -0x260 | -32.54e100 | 3e+26J | -052318172735L |
| 0x69 | 70.2-E12 | 4.53e-7j | -4721885298529L |

------
## Stringhe

<div style="text-align: justify;">
Le stringhe in Python sono identificate come un insieme contiguo di caratteri rappresentati tra virgolette (siano esse singole <code>'</code> o doppie <code>"</code>). Le parti di una stringa possono essere acquisite usando l'operatore di slice (<code>[]</code> e <code>[:]</code>). Più stringhe possono essere concatenate tramite l'operatore di concatenamento (<code>+</code>). Inoltre è consentita la ripetizione di una stringa utilizzando l'operatore di ripetizione (<code>*</code>). Ad esempio, lo script:
</div>
```python
str = 'Hello World!'

print(str)          # stampa l'intera stringa
print(str[0])       # stampa il primo carattere della stringa
print(str[2:5])     # stampa dal 3^ al 5^ carattere della stringa
print(str[2:])      # stampa la stringa a partire dal 3^ carattere
print(str * 2)      # stampa la stringa due volte
print(str + "TEST") # stampa le stringhe concatenate
```
<div style="text-align: justify;">
produrrà il risultato seguente:
</div>
```zsh
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
```

------
## Liste

<div style="text-align: justify;">
Le liste costituiscono il più versatile tipo di dati di Python. Una lista contiene elementi separati da virgole e racchiusi tra parentesi quadre (<code>[]</code>). In un certo senso, le liste sono simili agli array di C. Una differenza tra di loro è che gli elementi appartenenti a una lista possono essere di tipi diversi. <br>

&nbsp; Come per le stringhe, è possibile accedere ai valori memorizzati in una lista utilizzando l'operatore di slice (<code>[]</code> e <code>[:]</code>). Così pure l'operatore di concatenamento (<code>+</code>) e quello di ripetizione (<code>*</code>) possono essere usati, rispettivamente, per concatenare più liste e per ripetere il contenuto di una stessa lista. Ad esempio, lo script:
</div>
```python
list = ['abcd', 786 , 2.23, 'john', 70.2]
tiny_list = [123, 'john']

print(list)              # stampa l'intera lista
print(list[0])           # stampa il 1^ elemento della lista
print(list[1:3])         # stampa dal 2^ fino al 3^ elemento della lista
print(list[2:])          # stampa la lista a partire dal 3^ elemento
print(tiny_list * 2)     # stampa la lista due volte
print(list + tiny_list)  # stampa le liste concatenate
```
<div style="text-align: justify;">
produrrà il risultato seguente:
</div>
```zsh
['abcd', 786, 2.23, 'john', 70.2]
abcd
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
```

------
## Tuple

<div style="text-align: justify;">
Una tupla è un tipo di dati molto simile a una lista. Le principali differenze tra liste e tuple sono: 
<ul>
<li>le liste sono racchiuse tra parentesi quadre <code>[]</code>, mentre le tuple sono racchiuse tra parentesi tonde <code>()</code></li>
<li>gli elementi di una lista possono essere modificati, mentre gli elementi delle tuple non possono essere modificati (si tratta in sostanza di dati di sola lettura)</li>
</ul>
Per comprendere meglio quanto suddetto, forniamo due script. Nel primo, mettiamo in luce le somiglianze tra liste e tuple (unica differenza, l'uso delle parentesi tonde invece delle quadre):
</div>
```python
tupla = ('abcd', 786 , 2.23, 'john', 70.2)
tiny_tupla = (123, 'john')

print(tupla)                # stampa l'intera tupla
print(tupla[0])             # stampa il 1^ elemento della tupla
print(tupla[1:3])           # stampa dal 2^ fino al 3^ elemento della tupla
print(tupla[2:])            # stampa la tupla a partire dal 3^ elemento
print(tiny_tupla * 2)       # stampa la tupla due volte
print(tupla + tiny_tupla)   # stampa le tuple concatenate
```
<div style="text-align: justify;">
Eseguendo tale script, otterremo:
</div>
```zsh
('abcd', 786, 2.23, 'john', 70.2)
abcd
(786, 2.23)
(2.23, 'john', 70.2)
(123, 'john', 123, 'john')
('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
```
<div style="text-align: justify;">
Il secondo script mette in luce il fatto che le tuple si compongono di elementi di sola lettura:
</div>
```python
list = ['abcd', 786 , 2.23, 'john', 70.2]
tupla = ('abcd', 786 , 2.23, 'john', 70.2)

list[2] = 1000     # sintassi valida per le liste
tupla[2] = 1000    # sintassi invalida per le tuple
```
<div style="text-align: justify;">
Tale script, quando eseguito, produrrà il seguente messaggio di errore:
</div>
```zsh
TypeError: 'tuple' object does not support item assignment
```

------
## Dizionari

<div style="text-align: justify;">
I dizionari funzionano come array associativi e sono costituiti da coppie chiave-valore. Una chiave può essere di qualsiasi tipo, ma di solito sono numeri o stringhe. I valori, più delle chiavi, possono essere qualsiasi oggetto di Python.<br>

&nbsp; I dizionari sono racchiusi tra parentesi graffe <code>{}</code>, e i suoi valori possono essere assegnati e consultati usando parentesi quadre <code>[]</code>. Forniamo un esempio:
</div>
```python
dict = {}
dict['one'] = "This is one" 
dict[2]     = "This is two"

tiny_dict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one'])          # stampa il valore associato alla chiave 'one'
print(dict[2])              # stampa il valore associato alla chiave 2
print(tiny_dict)            # stampa l'intero dizionario
print(tiny_dict.keys())     # stampa l'elenco delle chiavi
print(tiny_dict.values())   # stampa l'elenco dei valori
```
<div style="text-align: justify;">
Tale script produrrà il risultato seguente:
</div>
```zsh
This is one
This is two
{'dept': 'sales', 'code': 6734, 'name': 'john'}
['dept', 'code', 'name']
['sales', 6734, 'john']
```
<div style="text-align: justify;">
Osserviamo infine che i dizionari non hanno alcun concetto di ordine tra gli elementi. Tuttavia, non è corretto dire che i suoi elementi sono disordinati; di fatto, tali elementi sono semplicemente non ordinati.
</div>

------
## Conversione dei tipi di dati

<div style="text-align: justify;">
A volte, potrebbe essere necessario eseguire conversioni tra i suddetti tipi predefiniti. Esistono diverse funzioni integrate (dette anche <i>built-in</i>) per eseguire la conversione da un tipo di dati a un altro. Queste funzioni restituiscono un nuovo oggetto che rappresenta il valore convertito. Forniamo di seguito una lista contenente alcune di queste funzioni integrate:
</div>

| **Funzione** | **Descrizione** |
| -- | -- |
| <code>int(x)</code> | converte <code>x</code> in un intero|
| <code>str(x)</code> | converte <code>x</code> in una stringa |
| <code>list(x)</code> | converte <code>x</code> in una lista |
| <code>tuple(x)</code> | converte <code>x</code> in una tupla |
| <code>dict(x)</code> | converte <code>x</code> in un dizionario |


<div style="text-align: justify;">
Infine, diamo un esempio in cui trasformiamo una stringa in un numero intero:
</div>
```python
# esempio di conversione di una stringa in un intero
x = "5"             # x è una stringa
y = 1000            # y è un intero
print(int(x) + y)   # tramutiamo x in un intero, che poi andiamo a sommare a y
```
<div style="text-align: justify;">
Tale script stamperà il risultato:
</div>
```zsh
1005
```

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">