# Metodi standard

<div style="text-align: justify;">
Nella precedente sezione abbiamo parlato di OOP e, in particolare, abbiamo visto che un oggetto è un'istanza di una classe. Abbiamo anche visto, nella sezione dedicata alla variabili, alcuni tipi standard. Ebbene, tali tipi sono essi stessi degli oggetti, che quindi dispongono di attributi e metodi, con questi ultimi che consentono agli sviluppatori, in molti casi, di non dover re-inventare la ruota. L'obiettivo di questa sezione è quindi quello di elencare i metodi principali dei seguenti tipi standard di variabili:
<ul>
<li>Stringhe</li>
<li>Liste</li>
<li>Dizionari</li>
</ul>
Per un elenco completo si rimanda alla documentazione ufficiale di Python.
</div>

---
## Stringhe

<div style="text-align: justify;">
Di seguito un elenco dei principali metodi associati ad oggetti di tipo stringa.
</div>
| **Metodo** | **Descrizione** | **Esempio** |
| -- | -- | -- |
| <code>capitalize()</code> | Converte il primo carattere in maiuscolo e i restanti in minuscolo. | <code>'aBc'.capitalize() == 'Abc'</code> |
| <code>lower()</code> | Converte tutti i caratteri in minuscolo. | <code>'ABC'.lower() == 'abc'</code> |
| <code>upper()</code> | Converte tutti i caratteri in maiuscolo. | <code>'abc'.upper() == 'ABC'</code> |
| <code>count()</code> | Conta quante volte una stringa è ripetuta in un'altra. | <code>'abcabc'.count('abc') == 2</code> |
| <code>find()</code> | Restituisce l'indice della prima occorrenza di una stringa in un'altra. | <code>'abca'.find('a') == 0</code> |
| <code>isalpha()</code> | Stabilisce se una data stringa è alfabetica. | <code>'abc'.isalpha() == True</code> |
| <code>isnumeric()</code> | Stabilisce se una data stringa è numerica. | <code>'123'.isnumeric() == True</code> |
| <code>split()</code> | Restituisce una lista con le parole della stringa. | <code>'a b c'.split() == ['a', 'b', 'c']</code> |
| <code>replace()</code> | Rimpiazza una sottostringa con un'altra. | <code>'abc'.replace('a', 'd') == 'dbc'</code> |

---
## Liste 

<div style="text-align: justify;">
Di seguito un elenco dei principali metodi associati ad oggetti di tipo lista.
</div>
| **Metodo** | **Descrizione** | **Esempio** |
| -- | -- | -- |
| <code>append()</code> | Aggiunge un elemento alla fine della lista. | <code>['a'].append('b') == ['a', 'b']</code> |
| <code>insert()</code> | Inserisce un elemento in una data posizione. | <code>['a', 'c'].insert(1, 'b') == ['a', 'b', 'c']</code> |
| <code>extend()</code> | Aggiunge gli elementi di una lista alla fine di un'altra lista. | <code>['a', 'b'].extend(['c', 'd']) == ['a', 'b', 'c', 'd']</code> |
| <code>remove()</code> | Rimuove un elemento dalla lista. | <code>['a', 'b'].remove('b') == ['a']</code> |
| <code>index()</code> | Restituisce il primo indice di un dato elemento nella lista. | <code>['a', 'b', 'a'].index('a') == 0</code> |
| <code>count()</code> | Conta quante volte è presente un dato elemento nella lista. | <code>['a', 'b', 'a'].count('a') == 2</code> |
| <code>pop()</code> | Elimina dalla lista l'elemento in un dato indice. | <code>['a', 'b', 'a'].pop(2) == ['a', 'b']</code> |
| <code>reverse()</code> | Inverte gli elementi della lista. | <code>['a', 'b', 'c'].reverse() == ['c', 'b', 'a']</code> |
| <code>sort()</code> | Ordina gli elementi della lista. | <code>['b', 'c', 'a'].reverse() == ['a', 'b', 'c']</code> |
| <code>clear()</code> | Elimina tutti gli elementi della lista. | <code>['a', 'b'].clear() == []</code> |
| <code>max()</code> | Restituisce il valore massimo nella lista. | <code>max([1, 4, 3]) == 4 </code> |
| <code>min()</code> | Restituisce il valore minimo nella lista. | <code>min([1, 4, 3]) == 1 </code> |
| <code>sum()</code> | Somma gli elementi della lista. | <code>sum([1, 4, 3]) == 8 </code> |

---
## Dizionari

<div style="text-align: justify;">
Di seguito un elenco dei principali metodi associati ad oggetti di tipo dizionario.
</div>
| **Metodo** | **Descrizione** | **Esempio** |
| -- | -- | -- |
| <code>keys()</code> | Restituisce una lista con le chiavi del dizionario. | <code>{'a': 1, 'b': 2}.keys() == ['a', 'b']</code> |
| <code>values()</code> | Restituisce una lista con i valori del dizionario. | <code>{'a': 1, 'b': 2}.values() == [1, 2]</code> |
| <code>clear()</code> | Rimuove tutti gli elementi del dizionario. | <code>{'a': 1, 'b': 2}.clear() == {}</code> |
| <code>update()</code> | Aggiorna il dizionario inserendo nuove coppie chiave-valore. | <code>{'a': 1, 'b': 2}.update({'c': 3}) == {'a': 1, 'b': 2, 'c': 3}</code> |


<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">