# Instrucciones

# Hacer un programa que juegue Piedra, papel o tijera, teniendo al usuario y
# la computadora como contrincantes

import time
from time import sleep
import random
#Creo una variable con la opciones que puedo elegir en el juego
opciones = ["piedra","papel","tijeras"]


print("bienvenido al juego de piedra papel o tijera!!")
print("---------------------------------------------")

#Uso un ciclo while para poder jugar las veces que quiera el juego, solo salgo una vez que cierre la consola
while True:
    usuario = input("Elije: piedra, papel o tijeras:")
    
    if usuario not in opciones:
        print("no existe la opcion seleccionada")
        continue
#Creo una variable que seria la pc, y di uso a la funcion de random.choise , que encontre googleando :), practicamente serviria para que la maquina elija aleatoriamente una de las opciones que tengo en mi lista.
    computadora = random.choice(opciones)
    sleep(0.9)
    print(f"la PC ha seleccionado {computadora}")
    sleep(0.9)

#Estas son mis condiciones que se deben de cumplir o no para tener algun resultado ya sea si pierdo o gano.
    if usuario == computadora:
        print(f"Empate!, ambos eligieron {usuario}")
    elif usuario == "piedra" and computadora == "tijeras":
        print(f"Ganaste!, {usuario} gana en contra de {computadora}")
    elif usuario == "tijeras" and computadora == "papel":
        print(f"Ganaste!, {usuario} gana en contra de {computadora}")
    elif usuario == "papel" and computadora == "piedra":
        print(f"Ganaste!, {usuario} gana en contra de {computadora}")
    else:
        print(f"Perdiste, {usuario} pierde contra {computadora}")
    sleep(0.9)
    
    print("fin del juego")
    print("--------------------------------------------------------")
    print("gracias por jugar :D")

#Uso la funcion sleep para poder darle un tiempo de espera al programa para dar algun resultado o que elija alguna opcion, para que sea mas dinamico mi juego.
#Llegando a este punto el juego ya tendria que ejecutarse correctamente :D
