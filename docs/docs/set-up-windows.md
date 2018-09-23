# Set-up (Windows 10)

<div style="text-align: justify;">
In questa sezione vedremo come installare Python 3 sul sistema operativo Windows 10, come creare un ambiente virtuale e infine come eseguire al suo interno un semplice script Python. 
</div>

------
## Installare Python 3

<div style="text-align: justify;">
Il primo passo è recarsi presso il <a href="https://www.python.org/downloads/">sito ufficiale</a> e scaricare il file eseguibile (estensione <code>exe</code>) necessario all'installazione di Python 3 (al tempo in cui scrivo, siamo alla versione 3.7.0). Terminato il download, lanciare il file eseguibile e, prima di procedere con l'installazione, selezionare la voce <strong>Add Python 3.7 to PATH</strong> (ciò consentirà al command prompt di riconoscere il comando <code>python</code>)<sup><a href="#fn0" id="ref0">1</a></sup>. A questo punto, cliccare su <strong>Install Now</strong> e seguire la procedura guidata che ci consentirà di terminare l'installazione di Python 3.
Ricapitoliamo schematicamente quanto appena detto attraverso il seguente slider.<br><br>

<div id="install_python3" class="carousel slide" data-interval="false">
  <ol class="carousel-indicators">
    <li data-target="#install_python3" data-slide-to="0" class="active"></li>
    <li data-target="#install_python3" data-slide-to="1"></li>
    <li data-target="#install_python3" data-slide-to="2"></li>
    <li data-target="#install_python3" data-slide-to="3"></li>
    <li data-target="#install_python3" data-slide-to="4"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="../img/win-1.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 1</h5>
            <p style="color: gray">Visitare la pagina di Download di Python</p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-2.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 2</h5>
            <p style="color: gray">Cliccare su <strong>Download Python 3.7.0</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-4.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 3</h5>
            <p style="color: gray">Lanciare l'eseguibile scaricato</p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-6.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 4</h5>
            <p style="color: gray">Selezionare la voce <strong>Add Python 3.7 to PATH</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-7.png">
        <div class="carousel-caption d-none d-md-block">
            <h5>Step 5</h5>
            <p style="color: gray">Cliccare <strong>Install Now</strong> e seguire la procedura guidata per terminare l'installazione</p>
        </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#install_python3" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#install_python3" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div><br>
</div>


------
## Creare l'ambiente virtuale

<div style="text-align: justify;">
È pratica comune utilizzare ambienti virtuali per qualsivoglia progetto Python. Un ambiente virtuale consente di creare uno spazio isolato di modo che si possa, ad esempio, utilizzare Python 2 e Python 3 per due diversi progetti ubicati nello stesso computer. È inoltre una buona norma quella di mantenere tutti i vostri ambienti virtuali in un'unica cartella, ad esempio nella cartella <code>virtualenvs</code> all'interno della cartella <code>home</code>, quest'ultima ubicata nel percorso <code>C:\Users\nomeutente</code> e generalmente indicata con il simbolo <code>~</code>. Detto questo, dopo aver aperto <strong>Command Prompt</strong>, possiamo creare la cartella <code>virtualenvs</code> ed entrare in essa eseguendo nel prompt i comandi seguenti:<sup><a href="#fn1" id="ref1">2</a></sup>
</div>
```zsh
~ > mkdir virtualenvs
~ > cd virtualenvs
virtualenvs >
```
<div style="text-align: justify;">
Si noti che col comando <code>mkdir virtualenvs</code> creiamo la cartella <code>virtualenvs</code> (di fatto <code>mkdir</code> è un diminutivo di <i>make directory</i>, ossia <i>crea la cartella</i>), mentre col comando <code>cd virtualenvs</code> entriamo all'interno della cartella <code>virtualenvs</code> (in tal caso <code>cd</code> è l'acronimo di <i>change directory</i>, ovvero <i>entra nella cartella</i>).<br>
&nbsp A questo punto, mediante l'ausilio del modulo <code>venv</code> incorporato in Python, possiamo inizializzare il nostro ambiente virtuale, che chiameremo <code>myvenv</code>:
</div>
```zsh
virtualenvs > python -m venv myvenv
```
<div style="text-align: justify;">
Il comando di cui sopra consente di generare una serie di cartelle e file, di modo che il nostro file system presenti, allo stato attuale, la struttura seguente:
</div>
```
~
|__virtualenvs
   |__myvenv
      |__Include
      |__Lib
      |__Scripts
      |__pyvenv.cfg
```
<div style="text-align: justify;">
Possiamo adesso entrare nella cartella <code>myvenv</code> e attivare l'ambiente virtuale tramite i comandi:
</div>
```zsh
virtualenvs > cd myvenv
myvenv > Scripts\activate
(myvenv) myvenv >
```
<div style="text-align: justify;">
Val la pena notare che quando l'ambiente virtuale è attivo, sarà possibile vedere il suo nome tra parentesi all'inizio della riga di comando. I moduli che andrete a installare saranno ora disponibili solo all'interno di questo specifico ambiente virtuale. Potrete utilizzare il comando <code>pip freeze</code> per vedere la lista di tutti i moduli installati all'interno dell'ambiente virtuale.<br>
&nbsp Per disattivare l'ambiente virtuale in esecuzione, si può chiudere direttamente il command prompt, oppure si può dare la seguente istruzione: 
</div>
```zsh
(myvenv) myvenv > deactivate
myvenv >
```
Nel seguente slider vi è infine una rappresentazione schematica dei passi sopra illustrati.

<div style="text-align: justify;">
<div id="venv" class="carousel slide" data-interval="false">
  <ol class="carousel-indicators">
    <li data-target="#venv" data-slide-to="0" class="active"></li>
    <li data-target="#venv" data-slide-to="1"></li>
    <li data-target="#venv" data-slide-to="2"></li>
    <li data-target="#venv" data-slide-to="3"></li>
    <li data-target="#venv" data-slide-to="4"></li>
    <li data-target="#venv" data-slide-to="5"></li>
    <li data-target="#venv" data-slide-to="6"></li>
    <li data-target="#venv" data-slide-to="7"></li>
    <li data-target="#venv" data-slide-to="8"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="../img/win-8.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 1</h5>
            <p style="color: gray">Digitare <strong>cmd</strong> sulla barra di ricerca e aprire <strong>Command Prompt</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-9.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 2</h5>
            <p style="color: gray">Siete adesso nella cartella <code>C:\Users\nomeutente</code>, detta cartella <code>home</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-10.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 3</h5>
            <p style="color: gray">Creare la cartella <code>virtualenvs</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-11.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 4</h5>
            <p style="color: gray">Entrare nella cartella <code>virtualenvs</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-12.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 5</h5>
            <p style="color: gray">Creare l'ambiente virtuale <code>myvenv</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-13.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 6</h5>
            <p style="color: gray">Entrare nella cartella <code>myvenv</code></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-14.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 7</h5>
            <p style="color: gray">Attivare l'ambiente virtuale</p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-16.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 8</h5>
            <p style="color: gray">Disattivare l'ambiente virtuale</p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/win-17.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 9</h5>
            <p style="color: gray">Visualizzare il contenuto dell'ambiente virtuale appena creato</p>
        </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#venv" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#venv" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div><br>
</div>

------
## Installare Sublime Text

<div style="text-align: justify;">
Per poter cominciare a programmare efficacemente in Python, occorre adesso fare affidamento a un IDE (<i>Integrated Development Environment</i>, anche detto <i>editor di testo</i>) adeguato. A tal fine, una soluzione gratuita e affidabile è <a href="https://www.sublimetext.com/">Sublime Text</a>, il cui file <code>exe</code> può essere scaricato dal sito ufficiale e poi installato tramite semplice procedura guidata. 
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
            <h5 style="color: gray">Step 1</h5>
            <p>Aprire l'IDE Sublime Text e selezionare <strong>File > Open Folder...</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-2.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 2</h5>
            <p>Scegliere la cartella <strong>~\virtualenvs\myvenv</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-3.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 3</h5>
            <p>Selezionare <strong>myvenv > New Folder</strong> e aggiungere la cartella <strong>src</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-4.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 4</h5>
            <p>Selezionare <strong>src > New File</strong> e aggiungere il file <strong>main.py</strong></p>
        </div>
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="../img/sublime-win-5.png">
        <div class="carousel-caption d-none d-md-block">
            <h5 style="color: gray">Step 5</h5>
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

Adesso che abbiamo a nostra disposizione il nostro primo script Python, potremo infine eseguirlo nel command prompt tramite la seguente successione di comandi:
</div>
```zsh
~ > cd virtualenvs\myvenv\
myvenv > Scripts\activate
(myvenv) myvenv > cd src
(myvenv) src > python main.py
Hello World.
```
<div style="text-align: justify;">
Si noti che: col comando <code>cd virtualenvs\myvenv\</code> si entra nella cartella <code>myvenv</code>; col comando <code>Scripts\activate</code> si attiva l'ambiente virtuale; col comando <code>cd src</code> si entra nella cartella <code>src</code> dove è ubicato lo script <code>main.py</code>; infine col comando <code>python main.py</code> si esegue il predetto script che, come possiamo vedere, stampa sulla linea di comando il messaggio <code>Hello World.</code>.


<hr>
<sup id="fn0">1. Se non si seleziona subito la voce <strong>Add Python 3.7 to PATH</strong>, bisognerà aggiungere manualmente, all'interno della variabile d'ambiente PATH, il percorso che punta all'interprete Python 3.7.
</sup><br>
<sup id="fn1">2. Si noti che, all'interno del prompt, la dicitura <code>folder ></code> indica che ci troviamo nella cartella <code>folder</code> del sistema operativo.
</sup><br>
</div>


<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
