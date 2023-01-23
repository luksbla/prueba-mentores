# Instrucciones

# Los estudiantes consultan la nota que recibirán según las calificaciones que obtuvieron

# Por ejemplo:

# Las calificaciones 4, 5, 3. Darán la nota 4
# Las calificaciones 3, 2, 5. Darán la nota 3.33

# Escribe algún código para determinar la nota de un estudiante

print("bienvendo al sistema de consulta de calificaciones")
print("---------------------------------------------------")
print("puede ingresar sus tres calificaciones para recibir el promedio de su nota final")

#Creo las variables de las 3 calificaciones a ingresar 
nota_ingresada_1 = int(input("ingrese su primera calificacion"))
nota_ingresada_2 =  int(input("ingrese su segunda calificacion"))
nota_ingresada_3 = int(input("ingrese su tercera calificacion"))
print("---------------------------------------------------------")


#Creo una variable llamada promedio para que divida mis notas ingresadas por 3, y eso me de el promedio de la nota
promedio = (nota_ingresada_1 + nota_ingresada_2 + nota_ingresada_3)/3

#Imprimo la nota y uso "%.2f" para que solo me muestre los primeros dos numeros de los decimales.
print("Su promedio de nota es: %.2f" %promedio)
print("GRACIAS POR UTILIZAR EL SISTEMA DE CONSULTA DE CALIFICACIONES")