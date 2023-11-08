import random
import sys
number = random.randint(0,100)
intentos = 0
aciertos = False
print (number)
while not aciertos:
    try:
        intento = int(input("Adivina el número aleatorio entre 0 y 99.¿Cual crees que es?"))
        intentos += 1
    except:
        print("Tienes que escribir el número")    
        sys.exit()
    if intento != number:
        if intento > number:
            print("Fallaste.El número es demasiado grande")
        else:
            print("Falleste.El número es demasiado pequeño")
    else:
        print("Ganaste. Has utilizado", intentos, "intentos")
        acierto=True
        break