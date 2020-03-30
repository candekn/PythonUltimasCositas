import time

###### Fibonacci ######
#Funcion:
def sucesion(num): 
    a = 0
    b= 1
    c=0
    print(0)
    for r in range(num):
        print(c)
        c = a+b
        a = b
        b = c
        time.sleep(0.5)
#'Main':
    
print("Bienvenido a la Sucesión de Fibonacci.")
while True:
    num = input("\nIngrese la cantidad de términos a mostrar (0 para terminar): ")
    try:
        num = int(num)
    except(ValueError,TypeError):
        num = 1
        print("\nIngrese un numero entero válido! ")
    if num==0:
        print("\nGracias por utilizar este programa by Cande.")
        break
    elif num<2:
        print("\nEl número ingresado debe ser mayor a 2.")
    else:
        sucesion(num)

    

