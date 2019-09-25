acumulado=int(0)
numero=str("")


#al colocar true como condicion de while, se forma un ciclo hasta que de forma explicita se utilice break
while True:
    numero=input("dame un numero entero: ")
    if numero=="":
        #si el numero es vacio, reporta la situacion y sale.
        print("vacio")
        break
    else:
        #si se proporciono valor, acumulado= acumulado + numero
        #se realiza el calculo usando suma incluyente (+=)
        #el += agrega el valor nuevo a la variable sin perder el anterior y se suman
        acumulado+=int(numero)
        salida="monto acumulado: {}"
        print(salida.format(acumulado))
