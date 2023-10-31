import time

def Ffor():
    print('este bucle repite algo de foma predefinida, en este caso 3 veces')
    for i in [1,2,3]: #pueden ser listas duplas diccionarios
        print(i,'hola mundo')
    
def Fwhile(j):
    print('\neste bucle se itera siempre que se cumpla una condicion \nen este caso el numero que se puso anteriormente')
    a=0
    while a < j:
        print(a+1,' hola mundo')
        a=a+1

menu="""
seleccione
1 for
2 while
3 salir
v
"""
# el programa corre en un do while ¯\_(ツ)_/¯ ahi esta el tercer ciclo
while True:
    sw=int(input(menu))
    if sw == 1:
        Ffor()
    elif sw == 2:
        Fwhile(int(input("cuantas veces quere ver hola mundo escrito?  :" )))
    elif sw == 3:
        break
    else:
        print('invalid number try again')
    time.sleep(2)
print('bye bye')
