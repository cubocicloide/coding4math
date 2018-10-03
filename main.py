def my_func():
    global x
    x = 10
    print("Il valore di x nella funzione è: ", x)

x = 20
my_func()
print("Il valore di x fuori dalla funzione è: ", x)