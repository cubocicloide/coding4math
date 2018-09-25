# Shell interattiva

<div style="text-align: justify;">
La seguente shell interattiva consente, a chi non fosse stato in grado di mettere a punto il proprio dispositivo, di poter cominciare a programmare in Python. Per poterla usare, basterà semplicemente scrivere il codice nella colonna <code>script.py</code>, e poi eseguirlo cliccando sul pulsante <code>Run</code>. L'output dello script sarà infine visualizzato nella colonna <code>IPython Shell</code>.

<input type="text" name="foo" id="input" value="" />
</div>

---

<div data-datacamp-exercise data-lang="python" data-height="570px" >
    <code data-type="sample-code" >
    print('Hello World')
    </code>
</div>


---

<div data-datacamp-exercise data-lang="python" data-height="570px" >
    <code data-type="sample-code" >
from urllib.request import urlopen

import json
import matplotlib.pyplot as plt
import numpy as np

url_base = 'https://api.weatherbit.io/v2.0/forecast/daily?'
postal_code = '72100'
country = 'IT'
key = 'a2e592329c9549dc8906aa5b9e84fc3b'

url = url_base + 'postal_code=' + postal_code \
            + '&country=' + country \
            + '&key=' + key

try:
    data = json.loads(urlopen(url).read().decode('utf-8'))
except:
    print('[ERROR] Invalid postal code or country code.')
else:
    # plot the minimum and the maximum temperature as function of the days
    day = np.zeros((len(data['data']),1))
    temp = np.zeros((len(data['data']),2))
    for i in range(0,len(data['data'])):
        day[i] = i
        temp[i][0] = data['data'][i]['min_temp']
        temp[i][1] = data['data'][i]['max_temp']

    fig, ax = plt.subplots()
    ax.plot(day, temp[:,0])
    ax.plot(day, temp[:,1])

    ax.set(xlabel='Days', 
           ylabel='Temperature range', 
           title= data['city_name'] + ': 16 days weather forecast')
    ax.grid()

    # show the results
    plt.show()


    </code>
</div>






<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">


<script type="text/javascript" src="//cdn.datacamp.com/dcl-react.js.gz"></script>
