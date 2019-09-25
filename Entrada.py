entrada=input()
print(type(entrada))
#se declara una variable booleana para verificar los datos si son enteros o
#son string en este caso se usa el isdigit que devuelve todas true si todos los caracteres de la cadena son digitos
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
#se hace la verificacion

if (esEntero):
	print("dato entero. ¡Muy bien!")
# si no  es entero entonces es cadena
else:
	print("dato no es entero. intentar de nuevo")