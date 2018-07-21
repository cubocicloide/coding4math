# Set-up (Mac OS High Sierra)

<div style="text-align: justify;">
In questa sezione vedremo come installare Python 3 sul sistema operativo Mac OS High Sierra, come creare un ambiente virtuale e infine come eseguire al suo interno un semplice script Python. 
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
Per installare Python 3 faremo uso del package manager <a href="https://brew.sh/">Homebrew</a>. Quest'ultimo dipende dal software <a href="https://en.wikipedia.org/wiki/Xcode">Xcode</a> distribuito gratuitamente da Apple. Abbiamo quindi bisogno di integrare Xcode nel nostro sistema, e possiamo farlo tramite la seguente istruzione da riga di comando:
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
## Creare l'ambiente virtuale

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

------
## Installare Sublime Text

<div style="text-align: justify;">
Per poter cominciare a programmare efficacemente in Python, occorre adesso fare affidamento a un IDE (Integrated Development Environment) adeguato. A tal fine, una soluzione gratuita e affidabile è <a href="https://www.sublimetext.com/">Sublime Text</a>, il cui file <code>dmg</code> può essere scaricato dal sito ufficiale e poi installato tramite semplice esecuzione. 
</div>

------
## Eseguire uno script

<div style="text-align: justify;">
Nel seguente slider, viene sintetizzata la procedura per scrivere, tramite Sublime Text, uno script Python denominato <code>main.py</code>, il quale stamperà sulla linea di comando la scritta <code>Hello World.</code>. <br><br>

<div id="carouselExampleIndicators" class="carousel slide" data-interval="false">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="../img/sublime-1.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 1</h5>
            <p>Aprire l'IDE Sublime Text e selezionare <code>File > Open...</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-2.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 2</h5>
            <p>Scegliere la cartella <code>~/virtualenvs/myvenv</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-4.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 3</h5>
            <p>Selezionare <code>myvenv > New Folder</code> e aggiungere la cartella <code>src</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-7.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 4</h5>
            <p>Selezionare <code>src > New File</code> e aggiungere il file <code>main.py</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-8.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 5</h5>
            <p>In <code>main.py</code> scrivere il codice <code>print('Hello World.')</code> e salvare</p>
        </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div><br>

Adesso che abbiamo a nostra disposizione il nostro primo script Python, potremo infine eseguirlo tramite la seguente successione di comandi:
</div>
```zsh
➜ ~  source ~/virtualenvs/myvenv/bin/activate
(myvenv) ➜ ~  cd virtualenvs/myvenv/src
(myvenv) ➜ src  python main.py
Hello World.
```
<div style="text-align: justify;">
Si noti che: col comando <code>source ~/virtualenvs/myvenv/bin/activate</code> si attiva l'ambiente virtuale; col comando <code>cd virtualenvs/myvenv/src</code> si entra nella cartella <code>src</code> dove è ubicato lo script <code>main.py</code>; infine col comando <code>python main.py</code> si esegue il predetto script che, come possiamo vedere, stampa sulla linea di comando il messaggio <code>Hello World.</code>.
<hr>
<sup id="fn0">1. Si noti che i simboli <code>➜ ~</code> indicano che ci troviamo nella home directory del sistema operativo.</sup><br>
<sup id="fn1">2. La installazione di Xcode potrebbe richiedere da pochi minuti ad alcune ore.</sup><br>
<sup id="fn2">3. Il comando di installazione di Homebrew è reperibile anche presso il sito ufficiale di Homebrew.</sup>
</div>


<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

