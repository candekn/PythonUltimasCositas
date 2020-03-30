#Multiplos
#Funcion:
def multiplos(num):
    num=num+1 #Le sume +1 porque el range empieza a contar desde 0
    for i in range(num):
        if(i%3==0 and i%5==0):
            print(i)
            
#Main:

print("Bienvenido a Multiplos de 3 y 5")
while True:
    num = input("\nIngrese un numero maximo (0 para terminar): ")
    try:
        num = int(num)
    except(ValueError,TypeError):
        print("\nIngrese un numero entero válido! ")
    if num=='0' or num==0:
        print("\nGracias por utilizar este programa by Cande.")
        break
    elif not isinstance (num,(int)):
        print("No está permitido ingresar letras o decimales")
    else:
        multiplos(num)
    