numero1=input("Numero1: ")
numero2=input("Numero2: ")
#se declara una variable para acomodar los datos solicitados y darles salida en un orden
salida=("Numeros proporcionados: {} y {}. {} ")
#se hace la comparacion si son iguales arroje la salida son iguales
if (numero1==numero2):
	print(salida.format(numero1,numero2,"Los numeros son iguales"))
#si los numeros son diferentes hara una comprobacion
else:
	#si el dato primero es mayor arroja que es mayor
	if numero1 > numero2:
		print(salida.format(numero1,numero2,"El numero primero es mayor"))
		#si el segundo es mayor arroja que ese se mayor
	else:
		print(salida.format(numero1,numero2,"el numero segundo es mayor"))