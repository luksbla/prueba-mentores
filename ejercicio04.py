# Instrucciones

# Un número Armstrong es un número que es la suma de sus propios dígitos
# elevados cada uno a la potencia de la cantidad de dígitos.


# Por ejemplo:

#     9 es un número de Armstrong, porque 9 = 9^1 = 9
#     10 no es un número de Armstrong, porque 10 != 1^2 + 0^2 = 1
#     153 es un número de Armstrong, porque 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#     154 no es un número de Armstrong, porque: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

# Escribe algún código para determinar si un número es un número Armstrong.

#Defino una funcion y le doy como parametro el numero que se va a ingresar

def num_armstrong (numero):

#Ya que se tendria que acceder a cada elemento de cada numero convierto a str para poder tener acceso a los elementos. 

    conversion = str(numero)
    contador = 0 

#Creo un ciclo for para ir acumulando los procesos y tambien para poder sumar, pude saber mas sobre esto gracias a google :D.

    for i in range(len(conversion)):
        contador = contador + (int(conversion[i]) ** len(conversion))


#Le doy condiciones a mi programa para que si un numero es armstrong me pueda devolver "True" y si no es me devuelva "False"

    if contador == numero:
        return True
    else:
        return False

#Por ultimo ejecuto el programa con el numero inresado.

print(num_armstrong(126))
