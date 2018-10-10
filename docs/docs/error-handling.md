# Gestione degli errori

<div style="text-align: justify;">
In questa sezione spiegheremo come gestire gli eventuali errori che si presentano durante l'esecuzione del nostro codice Python. In particolare, vedremo cosa è una eccezione, come sollevarla e infine come gestirla.
</div>

---
## Eccezioni

<div style="text-align: justify;">
Un'eccezione è un evento che si verifica durante l'esecuzione di un programma e che ne interrompe il normale flusso delle istruzioni. In generale, quando uno script Python incontra una situazione a cui non può far fronte, solleva un'eccezione. 

In particolare, quando un'eccezione viene sollevata, è necessario gestirla immediatamente, altrimenti l'esecuzione termina prima del previsto. Per comprendere meglio quanto detto, consideriamo lo script seguente:
</div>
```python
"""
Questo programma considera una lista di dividendi e una lista
di divisori, e poi inserisce i risultati di ciascuna divisione
in una lista di risultati.
"""

# definiamo le liste di dividendi e divisori
dividendo = [1,24,3,12]
divisore = [1,2,0,4]

# inizializziamo i risultati a None
risultato = [None, None, None, None]

# iteriamo sulle liste per calcolare il risultato
for i in range(len(dividendo)):
    risultato[i] = dividendo[i] / divisore[i]
print(risultato)
```
<div style="text-align: justify;">
Se proviamo ad eseguirlo, otterremo il seguente messaggio di errore:
</div>

```zsh
Traceback (most recent call last):
  File "script.py", line 16, in <module>
    risultato[i] = dividendo[i] / divisore[i]
ZeroDivisionError: division by zero
```
<div style="text-align: justify;">
Possiamo vedere che è stata sollevata l'eccezione <code>ZeroDivisionError</code>, questo perchè nel terzo ciclo di iterazione <code>divisore[2] = 0</code>. In particolare, l'esecuzione si è subito interrotta, senza dare la possibilità di terminare il ciclo di iterazioni, né tantomeno di stampare il risultato delle divisioni. In gergo si dice che il programma si è chiuso inaspettatamente, o che ha crashato. Vogliamo quindi evitare questo comportamento gestendo opportunamente l'errore che si è presentato. Vedremo nelle prossime sottosezioni come fare.
</div>

---
## Le eccezioni standard
<div style="text-align: justify;">
Prima di proseguire con la gestione delle eccezioni, proponiamo un elenco delle principali eccezioni standard incluse in Python. Per un elenco completo, si consiglia di visualizzare la documentazione ufficiale di Python.
</div>

| **Eccezione** | **Descrizione** | 
| -- | -- |
| <strong>Exception</strong> | Classe base per tutte le eccezioni |
| <strong>IndentationError</strong> | Sollevata quando vi è un errore di indentazione |
| <strong>SyntaxError</strong> | Sollevata quando è presente un errore di sintassi |
| <strong>NameError</strong> | Sollevata quando un identificatore non viene trovato nel namespace |
| <strong>ValueError</strong> | Sollevata quando il valore fornito a una funzione non è valido |
| <strong>IndexError</strong> | Sollevata quando un indice non viene trovato nella sequenza |
| <strong>KeyError</strong> | Sollevata quando una specifica chiave non è presente nel dizionario |
| <strong>AritmeticError</strong> | Classe base per tutte le eccezioni che riguardano calcoli numerici |
| <strong>ZeroDivisionError</strong> | Sollevata quando si cerca di dividere un numero per zero |
| <strong>FloatingPointError</strong> | Sollevata quando un calcolo a virgola mobile fallisce | 
| <strong>OverflowError</strong> | Sollevata quando un numero eccede il limite massimo previsto |

---
## <code>try...except...else...finally</code> 
<div style="text-align: justify;">
A questo punto vediamo come sfruttare l'istruzione <code>try...except...else...finally</code> per gestire i nostri errori. Anzitutto, la sintassi prevista per il suo utilizzo è:
</div>
```python
try:
    blocco try
except Exception:
    blocco except
else:
    blocco else
finally:
    blocco finally
```
<div style="text-align: justify;">
La logica del suddetto statement è la seguente: il programma prova (ossia <code>try</code>) ad eseguire le istruzioni contenute nel <code>blocco try</code>; se durante la sua esecuzione viene sollevata l'eccezione <code>Exception</code>, viene eseguito il <code>blocco except</code>; se invece non viene sollevata alcuna eccezione, viene eseguito il <code>blocco else</code>; infine, viene sempre eseguito il <code>blocco finally</code>. Il seguente diagramma di flusso sintetizza quanto appena detto.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="../img/try-except-else-finally.svg" style="width: 250px;"><br><br>
In maniera simile a quanto accade con lo statement <code>elif</code>, è possibile introdurre più di un blocco <code>except</code>, in modo da gestire diverse tipologie di eccezioni. Inoltre, gli statement <code>else</code> e <code>finally</code> sono opzionali.<br>
&nbsp; A questo punto siamo pronti a correggere lo script visto in precedenza:
</div>
```python
"""
Questo programma considera una lista di dividendi e una lista
di divisori, e poi inserisce i risultati di ciascuna divisione
in una lista di risultati.
"""

# definiamo le liste di dividendi e divisori
dividendo = [1,24,3,12]
divisore = [1,2,0,4]

# inizializziamo i risultati a None
risultato = [None, None, None, None]

# iteriamo sulle liste per calcolare il risultato
for i in range(len(dividendo)):
    try:
        risultato[i] = dividendo[i] / divisore[i]
    except ZeroDivisionError:
        print('[ERRORE] Il divisore non può essere uguale a 0.')
print(risultato)
```
<div style="text-align: justify;">
Stavolta, mandando in esecuzione il programma, otterremo l'output:
</div>
```zsh
[ERRORE] Il divisore non può essere uguale a 0.
[1.0, 12.0, None, 3.0]
```
<div style="text-align: justify;">
Si noti in particolare come l'intero ciclo di esecuzione del programma viene completato, nonostante la presenza di un divisore pari a zero. Abbiamo quindi evitato l'interruzione inaspettata dello script e, al contempo, abbiamo fornito un messaggio di errore significativo.
</div>

---
## <code>raise</code>

<div style="text-align: justify;">
Chiudiamo questa sezione spiegando come sollevare una eccezione. La keyword introdotta a tal fine dal linguaggio Python è <code>raise</code>. La sintassi per il suo utilizzo è:
</div>
```python
raise Exception
```
<div style="text-align: justify;">
dove <code>Exception</code> identifica il tipo di eccezione da sollevare (as es., <code>ValueError</code>). Possiamo quindi modificare il precedente script in modo da fornire una gestione più completa dell'errore, in cui è il programmatore, e non l'interprete, a sollevare l'eccezione:
</div>
```python
def dividi(x,y):
    """
    Questa funzione implementa la divisione x / y, accertandosi che il divisore 
    non sia nullo, e sollevando una eccezione qualora lo sia.
    """
    if y == 0:
        raise ValueError('[ERRORE] Il divisore non può essere uguale a 0.')
    return x / y

dividendo = [1,24,3,12]
divisore = [1,2,0,4]
risultato = [None, None, None, None]

for i in range(len(dividendo)):
    try:
        risultato[i] = dividi(dividendo[i],divisore[i])
    except ValueError as error:     # utilizziamo un alias per poter stampare il messaggio di errore
        print(error)     
print(risultato)
```
<div style="text-align: justify;">
In questo script abbiamo definito la funzione <code>dividi()</code> in cui viene implementata la divisione di due numeri. All'interno della funzione viene verificato che il divisore sia non nullo e, qualora lo sia, viene sollevata l'eccezione <code>ValueError</code>, in cui si specifica il relativo messaggio di errore. Eseguendo lo script, otterremo il seguente risultato:
</div>
```python
[ERRORE] Il divisore non può essere uguale a 0.
[1.0, 12.0, None, 3.0]
```

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">