# Set-up (Mac OS High Sierra)

<div style="text-align: justify;">
In questa sezione vedremo come installare Python 3 sul sistema operativo Mac OS High Sierra. Ci sono numerose strade per installare Python 3, le quali includono il download diretto dal <a href="https://www.python.org/downloads/">sito ufficiale</a>; tuttavia raccomando fortemente l'utilizzo del package manager <a href="https://brew.sh/">Homebrew</a>, il quale ci consentirà di semplificare la procedura di messa a punto del nostro dispositivo.
</div>

------
## Verificare la versione

<div style="text-align: justify;">
Anche se Python 2 è installato di default sui computer Apple, Python 3 non lo è. Potrete averne conferma eseguendo nel <a href="https://en.wikipedia.org/wiki/Terminal_(macOS)">Terminal</a> il seguente comando<sup><a href="#fn0" id="ref0">1</a></sup>:
</div>
```zsh
➜ ~  python --version
Python 2.7.10
```
<div style="text-align: justify;">
Per verificare se Python 3 è già installato, potete provare a eseguire <code>python3 --version</code>. Molto probabilmente otterrete un messaggio di errore; anche qualora abbiate una versione di Python 3, l'obiettivo è installare quella più recente.
</div>

------
## Installare Xcode e Homebrew

<div style="text-align: justify;">
Per installare Python 3 faremo uso del package manager Homebrew. Quest'ultimo dipende dal software <a href="https://en.wikipedia.org/wiki/Xcode">Xcode</a> distribuito gratuitamente da Apple. Abbiamo quindi bisogno di integrare Xcode nel nostro sistema, e possiamo farlo tramite la seguente istruzione da riga di comando:
</div>
```zsh
➜ ~  xcode-select --install
```
<div style="text-align: justify;">
Durante il processo di installazione, accettare tutte le condizioni proposte<sup><a href="#fn1" id="ref1">2</a></sup>. 
Il passo successivo consiste nell'installare Homebrew<sup><a href="#fn2" id="ref2">3</a></sup>:
</div>
```zsh
➜ ~  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
<div style="text-align: justify;">
Per verificare la corretta installazione di Homebrew, eseguire infine il comando seguente:
</div>
```zsh
➜ ~  brew doctor
Your system is ready to brew.
```

------
## Installare Python 3

<div style="text-align: justify;">
Per installare l'ultima versione di Python 3, dare la seguente istruzione:
</div>
```zsh
➜ ~  brew install python3
```
<div style="text-align: justify;">
A questo punto, potete verificare quale versione di Python 3 è stata resa disponibile:
</div>
```zsh
➜ ~  python3 --version
Python 3.7.0
```
<div style="text-align: justify;">
Per aprire la shell di Python 3 dalla linea di comando, basterà semplicemente scrivere <code>python3</code> e dare invio:
</div>
```zsh
➜ ~  python3
Python 3.7.0 (default, Jun 29 2018, 20:13:13)
[Clang 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
<div style="text-align: justify;">
Per uscire dalla shell di Python 3, bisognerà dare il comando <code>exit()</code>.
Si potrà inoltre ancora sfruttare Python 2, che era installato di default, tramite l'istruzione <code>python</code>:
</div>
```zsh
➜ ~  python
Python 2.7.15 (default, Jun 17 2018, 12:46:58)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

------
## Ambienti virtuali

<div style="text-align: justify;">
È pratica comune utilizzare ambienti virtuali per qualsivoglia progetto Python. Un ambiente virtuale consente di creare uno spazio isolato di modo che si possa, ad esempio, utilizzare Python 2 e Python 3 per due diversi progetti ubicati nello stesso computer. È inoltre una buona norma quella di mantenere tutti i vostri ambienti virtuali in un'unica cartella, ad esempio nella cartella <code>virtualenv/</code> all'interno della home directory. Creiamo quindi tale cartella:
</div>
```zsh
➜ ~  mkdir ~/virtualenvs
```
<div style="text-align: justify;">
Mediante l'ausilio del modulo <code>venv</code> incorporato in Python, possiamo inizializzare il nostro ambiente virtuale, che chiameremo <code>myvenv</code>:
</div>
```zsh
➜ ~  python3 -m venv ~/virtualenvs/myvenv
```
<div style="text-align: justify;">
Avendo utilizzato il termine <code>python3</code>, il nostro ambiente virtuale riconosce che quando digitiamo <code>python</code> per assegnare un comando, intendiamo utilizzare Python 3, non Python 2. Per attivare l'ambiente virtuale appena inizializzato, sarà sufficiente eseguire:
</div>
```zsh
➜ ~  source ~/virtualenvs/myvenv/bin/activate
(myvenv) ➜ ~
```
<div style="text-align: justify;">
Val la pena notare che quando l'ambiente virtuale è attivo, sarà possibile vedere il suo nome tra parentesi all'inizio della riga di comando. I moduli che andrete a installare saranno ora disponibili solo all'interno di questo specifico ambiente virtuale. Potrete utilizzare il comando <code>pip freeze</code> per vedere la lista di tutti i moduli installati all'interno dell'ambiente virtuale. 
<br>
Per disattivare l'ambiente virtuale in esecuzione, si può chiudere direttamente la finestra del Terminal, oppure si può dare la seguente istruzione: 
</div>
```zsh
(myvenv) ➜ ~  deactivate
➜ ~
```
<div style="text-align: justify;">
A questo punto, gli utenti Mac sono pronti a utilizzare il proprio dispositivo per realizzare i loro progetti Python 3.
<hr>
<sup id="fn0">1. Si noti che i simboli <code>➜ ~</code> indicano che ci troviamo nella home directory del sistema operativo.<a href="#ref0">↩</a></sup><br>
<sup id="fn1">2. La installazione di Xcode potrebbe richiedere da pochi minuti ad alcune ore.<a href="#ref1">↩</a></sup><br>
<sup id="fn2">3. Il comando di installazione di Homebrew è reperibile anche presso il sito ufficiale di Homebrew.<a href="#ref2">↩</a></sup>
</div>