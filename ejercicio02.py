# Instrucciones

# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase, seguido
# del porcentaje de veces que aparecela frase y el **porcentaje** de veces que aparece
# la letra en la frase.

# print("BIENVENIDO AL CONTADOR DE LETRAS 3000 :D")
# print("---------------------------------------")

# letra = (input("ingrese la letra que desea buscar:"))
# frase_usuario =[(input("favor ingresar una frase:"))]

# porcentaje = frase_usuario/100*letra


# print(f"la cantidad de veces que aparece la letra es:", frase_usuario.count(letra) )


# print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS, VUELVA PRONTO")
# print("----------------------------------------")


print("BIENVENIDO AL CONTADOR DE LETRAS 3000 :D")
print("---------------------------------------")

contador = 0
letra = (input("ingrese la letra que desea buscar:"))
frase_usuario = (input("favor ingresar una frase:"))
frase_separada = list(frase_usuario)

for letra_iterable in frase_separada:
      if letra_iterable in frase_separada:
            contador = contador + 1
            
      
porcentaje = contador / len(letra_iterable) * 100


print("la cantidad de veces que aparece la letra es:", frase_usuario.count(letra) )
print("el porcentaje de veces que aparecio la letra es del:", porcentaje , "%")

print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS, VUELVA PRONTO")
print("----------------------------------------")
   
