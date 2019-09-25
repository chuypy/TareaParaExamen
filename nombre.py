nombre=input("nombre: ")
apellidos=input("apellidos: ")
#en esta variable se junta las dos variables solicitadas

nombreCompleto=nombre+" "+apellidos


#en esta aparte de juntar las dos variables utiliza el .upper que convierte las letras minusculas en mayusculas su contrario es lower que convierte todo en minusculas
nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)