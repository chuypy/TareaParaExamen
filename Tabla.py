numero=input("que tabla de multiplicar quieres? ")
numero=int(numero)

#se ejecuta un ciclo for en la que el valor de numero sea multplicado por cada valor de i
#la salida es el numero el i y la multplicacion ya echa

for i in range(1,11):
    salida="la salida es {} x{} = {} "
    print(salida.format(numero,i,i*numero))

