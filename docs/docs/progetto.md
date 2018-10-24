# Progetto finale

### Esempio di rubrica scritta in formato <code>.json</code> (nome file: <code>rubrica.json</code>)
```json
{"contatti": [
    {"cognome": "Notarnicola", 
     "nome": "Ivano", 
     "cellulare": "3327493810"}, 
    {"cognome": "Sasso", 
     "nome": "Francesco", 
     "cellulare": "3348975936"}, 
    {"cognome": "Spedicato", 
     "nome": "Sara", 
     "cellulare": "3384414186"}
    ]
}
```

### Leggere da e scrivere su <code>rubrica.json</code> (nome modulo: <code>rubrica.py</code>)
```python
"""
Questo modulo si occupa di leggere e scrivere dati sul file rubrica.json
"""

# importo il modulo json necessario caricare i dati contenuti in rubrica.json
import json

# path dove è ubicato il file di rubrica (i.e., rubrica.json)
RUBRICA = './rubrica.json'

def leggi():
    """
    Questa funzione si occupa di leggere il contenuto della RUBRICA
    """
    with open(RUBRICA) as json_data:
        elenco = json.load(json_data)
    return elenco

def scrivi(elenco):
    """
    Questa funzione si occupa di scrivere sulla RUBRICA
    """
    with open(RUBRICA, 'w') as outfile:  
        json.dump(elenco, outfile)

# testiamo il modulo
if __name__=="__main__":

    # preleviamo l'elenco dei contatti dalla RUBRICA
    elenco = leggi()

    # aggiungiamo un nuovo contatto nell'elenco
    contatto = { "nome": "Biagio",
                 "cognome": "Faleni",
                 "cellulare": 3387985594 }
    elenco["contatti"].append(contatto)

    # stampiamo il nuovo elenco di contatti
    print(elenco["contatti"])

    # scriviamo il nuovo elenco nella RUBRICA
    scrivi(elenco)

```
<div style="text-align: justify;">

<!-- <div data-datacamp-exercise data-lang="python" data-height="650px" >
    <code data-type="sample-code" >
from urllib.request import urlopen

import json
import matplotlib.pyplot as plt
import numpy as np

"""
16 days forecast api-endpoint (see https://www.weatherbit.io/api/weather-forecast-16-day)
example: 
https://api.weatherbit.io/v2.0/forecast/daily?postal_code=72015&country=IT&key=a2e592329c9549dc8906aa5b9e84fc3b
"""

url_base = 'https://api.weatherbit.io/v2.0/forecast/daily?'
postal_code = '72100'   # Brindisi
country = 'IT'          # Italia
key = 'a2e592329c9549dc8906aa5b9e84fc3b'

url = url_base + 'postal_code=' + postal_code \
               + '&country=' + country \
               + '&key=' + key

# try to open the url
try:
    data = json.loads(urlopen(url).read().decode('utf-8'))
# if no data are given in the response, print the exception raised
except Exception as error:
    print(error)
# otherwise, parse the data contained in the response, and plot them
else:
    # plot minimum and maximum temperature as function of days
    day = np.zeros((len(data['data']),1))
    temperature = np.zeros((len(data['data']),2))
    for i in range(0,len(data['data'])):
        day[i] = i
        temperature[i][0] = data['data'][i]['min_temp']
        temperature[i][1] = data['data'][i]['max_temp']

    fig, ax = plt.subplots()
    ax.plot(day, temperature[:,0])
    ax.plot(day, temperature[:,1])

    ax.set(xlabel='Days', 
           ylabel='Temperature range', 
           title= data['city_name'] + ': 16 days weather forecast')
    ax.grid()

    # show the results
    plt.show()
    
    </code>
</div>  -->


</div>


<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">


<script type="text/javascript" src="//cdn.datacamp.com/dcl-react.js.gz"></script>