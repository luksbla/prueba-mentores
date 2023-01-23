# Instrucciones

#Crear una funcion para validación de nombres de usuarios.
#Dicha funcion deberá validar lo siguiente:

# - El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
# - El nombre de usuario debe ser alfanumérico.
# - Nombre de usuario con menos de 6 caracteres, retorna el mensaje 'El nombre de usuario debe contener al
# menos 6 caracteres'.
# - Nombre de usuario con más de 12 caracteres, retorna el mensaje 'El nombre de usuario no puede contener
# más de 12 caracteres'.
# - Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje 'El nombre de usuario
# puede contener solo letras y números'.
# - Nombre de usuario válido, retorna 'Correcto!'

print("bienvenido a orkut")
print("------------------")

#Creo las variables de los usuarios.
usuario_ingresado = input("por favor ingrese nombre de usuario")
caracteres = len(usuario_ingresado)

#Uso el metodo de ".isalnum" que encontre googleando, que basicamente me serviria para que se compruebe que los caracteres ingresados son alfanumericos
tipo = usuario_ingresado.isalnum()


#Le doy condiciones a mi programa para que se cumplan las intrucciones enviadas, o devuelvan algo incorrecto si se ingrese algun valor invalido.
if tipo == True:
    if caracteres < 6 :
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif caracteres > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    else:
         print("Correcto!", usuario_ingresado)
else:
    print("El nombre de usuario puede contener solo letras y números")

    
    

    

