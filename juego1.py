"""Primera parte. Importamos módulos y utilidades necesarias para el programa."""
import random
    # Importa la utilidad random para elegir el número aleatorio.
import sys
    # Importa la utilidad sys para tratar las excepciones.

"""Segunda parte. Definimos las variables y seleccionamos el número aleatorio."""
numero = random.randint(0,100)
    #Elije un número al azar entre 1 y 99, almacenandolo en la variable numero.
intentos = 0
    # Variable para sumar los intentos del jugador.
acierto = False
    # Variable booleana para indicar cuando se termina el juego.
#print (numero)
    #Esta línea la ejecutamos para conocer el número aleatorio y poder comprobar el funcionamiento del juego.

"""Tercera parte. Bucle con las opciones del juego."""
while not acierto:
#Iniciamos el primer bucle para contabilizar el número de intentos que necesita el jugador para adivinar el número.

    while True:
    # Iniciamos el segundo bucle para recoger el valor de cada intento y analizar que cumple las condiciones.
        try:
            intento = int(input("Adivina el número aleatotio entre 0 y 99. ¿Cual crees que es?"))
            #Asociamos el valor introducido por el jugador a la varible numérica "intento".
        except:
            print ("!Cuidado¡ No has escrito un número entero.")
            #Si por error el jugador escribe algo que no sea un número entero sale este mensaje.
            pass
            #Con "pass" se repite el segundo bucle apareciendo la pregunta del principio de nuevo.
        else:
        #Se ejecuta esta parte cuando el jugador introduce un número entero.
            if 0 <= intento <= 99:
            #Se ejecuta si el numero introducido está entre 0 y 99.
                intentos += 1
                break  # Salimos del segundo bucle.
            else:
            #Se ejecuta si el número introducido NO está entre 0 y 99.
                print("¡Error! El número que has escrito NO está entre 0 y 99")
                #Devuelve este mensaje indicando del error y se inicia el segundo bucle de nuevo.

    if intento != numero:
    #Si el "intento" del jugador es distinto del "numero" aleatorio. Volverá al primer bucle.
        if intento > numero:
        #Si el "intento" del jugador es mayor que el "numero" aleatorio.
            print("Fallaste. El número es demasiado grande")
        else:
        #Si el "intento" del jugador es menor que el "numero" aleatorio.
            print("Fallaste. El número es demasiado pequeño")
    else:
    #Se ejecuta en caso de que el jugador acierte el número. Se termina el juego.
        print("Ganaste. Has utilizado ",intentos," intentos")
        acierto=True
        #En esta ocasión en lugar de salir del bucle con "break" lo hacemos asignando el valor "True" a la variable booleana "acierto".