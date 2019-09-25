

#se genera un ciclo for que tendra los rangos que seran utilziados para seleccionar que tabla 
#se va a multplicar
for i in range(1,11):
    encabezado="tablad del {}"
    print(encabezado.format(i))
    print()
    #este ciclo for se utiliza sus rangos para saber por cuanto se va a multiplicar la variable i
    for j in range(1,11):
        salida="{} x {} = {}"
        #Aqui ya salen las dos variables con valores definidos y se multplican hasta completar las tablas hasta el 10
        print(salida.format(i,j,i*j))
    else:
        #el print solo es un salto de linea
        print()