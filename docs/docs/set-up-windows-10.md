# Set-up (Windows 10)

<div style="text-align: justify;">
In questa sezione vedremo come installare Python 3 sul sistema operativo Windows 10, come creare un ambiente virtuale e infine come eseguire al suo interno un semplice script Python. 
</div>

------
## Configurare PowerShell

<div style="text-align: justify;">
Il primo passo è eseguire come amministratore l'interfaccia a riga di comando denominata <a href="https://it.wikipedia.org/wiki/Windows_PowerShell">Powershell</a>. Per far ciò, sarà sufficiente cliccare col tasto destro l'icona di Powershell e selezionare l'opzione <strong>Esegui come Amministratore</strong>. A questo punto, per recarsi nella home directory, eseguire il comando<sup><a href="#fn0" id="ref0">1</a></sup>: 
</div>
```zsh
➜ system32  cd ~
➜ ~
```
<div style="text-align: justify;">
Nel seguente slider vi è una schematizzazione di quanto suddetto (si consiglia di evidenziare il testo se non visibile).<br><br>

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
      <img class="d-block w-100" src="../img/powershell-1.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 1</h5>
            <p>Nella barra di ricerca digitare <strong>PowerShell</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/powershell-2.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 2</h5>
            <p>Cliccare col tasto destro sull'icona <strong>Powershell</strong> e selezionare <strong>Esegui come Amministratore</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/powershell-3.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 3</h5>
            <p>Selezionare <strong>Sì</strong> nella successiva finestra</p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/powershell-4.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 4</h5>
            <p>Eseguire il comando <code>cd ~</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/powershell-5.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 5</h5>
            <p>Siamo ora nella cartella home, cioè <strong>C:\Users\nomeutente</strong></p>
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

Occorre adesso configurare PowerShell con permessi di esecuzione che consentano, all'utente corrente, il download di programmi fidati. A tal fine, settiamo la polizza di esecuzione dell'utente corrente a <strong>RemoteSigned</strong>. Per far ciò, eseguiamo il comando: 
</div>
```zsh
➜ ~  Set-ExecutionPolicy -Scope CurrentUser
```
<div style="text-align: justify;">
PowerShell ci chiederà di fornire una polizza di esecuzione che, nel nostro caso, è la seguente:
</div>
```zsh
➜ ~  RemoteSigned
```
<div style="text-align: justify;">
Una volta premuto invio, ci verrà chiesto se vogliamo cambiare la polizza di esecuzione. Digitare la lettera <code>y</code> per <strong>yes</strong>, consentendo così ai cambiamenti di avere effetto. Possiamo adesso procedere col download dei programmi che ci serviranno per mettere a punto il nostro ambiente di programmazione Python.
</div>

------
## Installare Chocolatey

<div style="text-align: justify;">
Per installare Python 3 faremo uso del package manager <a href="https://chocolatey.org/">Chocolatey</a>. Per scaricare Chocolatey, creiamo un oggetto Webclient che chiamiamo <code>$script</code>:
</div>
```zsh
➜ ~  $script = New-Object Net.WebClient
```
<div style="text-align: justify;">
Sfruttiamo poi tale oggetto per scaricare Chocolatey attraverso il comando:
</div>
```zsh
➜ ~  $script.DownloadString("https://chocolatey.org/install.ps1")
```
<div style="text-align: justify;">
Giunti qui, possiamo installare Chocolatey tramite l'istruzione:
</div>
```zsh
➜ ~  iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
```
<div style="text-align: justify;">
Infine, possiamo aggiornare Chocolatey in ogni istante futuro eseguendo dalla PowerShell il comando:
</div>
```zsh
➜ ~  choco upgrade chocolatey
```

------
## Installare Python 3

<div style="text-align: justify;">
Adesso che abbiamo a disposizione Chocolatey, possiamo installare Python 3 semplicemente eseguendo l'istruzione:
</div>
```zsh
➜ ~  choco install install -y python3
```
<div style="text-align: justify;">
Una volta terminato il processo di installazione, per verificare l'effettiva presenza di Python 3 nel nostro sistema operativo, chiudere e riaprire Powershell come Amministratore, poi digitare:
</div>
```zsh
➜ ~  python -V
```
<div style="text-align: justify;">
Dovremmo a questo punto ottenere un output recante la versione di Python installata sul sistema operativo:
</div>
```zsh
Output
Python 3.5.1
```
<div style="text-align: justify;">
Assieme a Python, sarà installato anche pip, il quale consente la gestione dei cosiddetti moduli Python. Ci assicuriamo che pip sia aggiornato alla versione più recente tramite l'istruzione:
</div>
```zsh
➜ ~  python -m pip install --upgrade pip
```
<div style="text-align: justify;">
Adesso che Python 3 è installato e pip è aggiornato, possiamo mettere a punto un ambiente virtuale per i nostri futuri progetti.
</div>


------
## Creare l'ambiente virtuale

<div style="text-align: justify;">
È pratica comune utilizzare ambienti virtuali per qualsivoglia progetto Python. Un ambiente virtuale consente di creare uno spazio isolato di modo che si possa, ad esempio, utilizzare Python 2 e Python 3 per due diversi progetti ubicati nello stesso computer. È inoltre una buona norma quella di mantenere tutti i vostri ambienti virtuali in un'unica cartella, ad esempio nella cartella <code>virtualenv</code> all'interno della home directory. Creiamo quindi tale cartella:
</div>
```zsh
➜ cartella  cd ~
➜ ~  mkdir virtualenvs
➜ ~  cd .\virtualenvs\
➜ virtualenvs
```
<div style="text-align: justify;">
Mediante l'ausilio del modulo <code>venv</code> incorporato in Python, possiamo inizializzare il nostro ambiente virtuale, che chiameremo <code>myvenv</code>:
</div>
```zsh
➜ virtualenvs  python -m venv myvenv
➜ virtualenvs  cd .\myvenv\
➜ myvenv
```
<div style="text-align: justify;">
Per attivare l'ambiente virtuale appena inizializzato, sarà sufficiente eseguire:
</div>
```zsh
➜ myvenv  Scripts\activate
(myvenv) ➜ myvenv
```
<div style="text-align: justify;">
Val la pena notare che quando l'ambiente virtuale è attivo, sarà possibile vedere il suo nome tra parentesi all'inizio della riga di comando. I moduli che andrete a installare saranno ora disponibili solo all'interno di questo specifico ambiente virtuale. Potrete utilizzare il comando <code>pip freeze</code> per vedere la lista di tutti i moduli installati all'interno dell'ambiente virtuale. 
<br>
Per disattivare l'ambiente virtuale in esecuzione, si può chiudere direttamente la finestra di PowerShell, oppure si può dare la seguente istruzione: 
</div>
```zsh
(myvenv) ➜ myvenv  deactivate
➜ myvenv
```

------
## Installare Sublime Text

<div style="text-align: justify;">
Per poter cominciare a programmare efficacemente in Python, occorre adesso fare affidamento a un IDE (Integrated Development Environment) adeguato. A tal fine, una soluzione gratuita e affidabile è <a href="https://www.sublimetext.com/">Sublime Text</a>, il cui file <code>exe</code> può essere scaricato dal sito ufficiale e poi installato tramite semplice esecuzione. 
</div>

------
## Eseguire uno script

<div style="text-align: justify;">
Nel seguente slider, viene sintetizzata la procedura per scrivere, tramite Sublime Text, uno script Python denominato <code>main.py</code>, il quale stamperà sulla linea di comando la scritta <code>Hello World.</code>. <br><br>

<div id="carouselExampleIndicators1" class="carousel slide" data-interval="false">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators1" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators1" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators1" data-slide-to="2"></li>
    <li data-target="#carouselExampleIndicators1" data-slide-to="3"></li>
    <li data-target="#carouselExampleIndicators1" data-slide-to="4"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="../img/sublime-win-1.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 1</h5>
            <p>Aprire l'IDE Sublime Text e selezionare <strong>File > Open Folder...</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-2.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 2</h5>
            <p>Scegliere la cartella <strong>~\virtualenvs\myvenv</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-3.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 3</h5>
            <p>Selezionare <strong>myvenv > New Folder</strong> e aggiungere la cartella <strong>src</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-4.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 4</h5>
            <p>Selezionare <strong>src > New File</strong> e aggiungere il file <strong>main.py</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-5.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 5</h5>
            <p>In <strong>main.py</strong> scrivere il codice <code>print('Hello World.')</code> e salvare</p>
        </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators1" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators1" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div><br>

Adesso che abbiamo a nostra disposizione il nostro primo script Python, potremo infine eseguirlo tramite la seguente successione di comandi:
</div>
```zsh
➜ cartella  cd ~
➜ ~  cd .\virtualenvs\myvenv\
➜ myvenv  Scripts\activate
(myvenv) ➜ myvenv  cd .\src\
(myvenv) ➜ src  python main.py
Hello World.
```
<div style="text-align: justify;">
Si noti che: col comando <code>cd ~</code> ci rechiamo presso la home directory; col comando <code>cd .\virtualenvs\myvenv\</code> si entra nella cartella <code>myvenv</code>; col comando <code>Scripts\activate</code> si attiva l'ambiente virtuale; col comando <code>cd .\src\</code> si entra nella cartella <code>src</code> dove è ubicato lo script <code>main.py</code>; infine col comando <code>python main.py</code> si esegue il predetto script che, come possiamo vedere, stampa sulla linea di comando il messaggio <code>Hello World.</code>.


<hr>
<sup id="fn0">1. Si noti che la scrittura <code>➜ cartella</code> indica che ci troviamo nella directory chiamata <code>cartella</code>, mentre il simbolo <code>~</code> indica la home directory del sistema operativo, solitamente ubicata in <code>C:\Users\nomeutente</code>.
</sup>


<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
