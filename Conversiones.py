numero="1234"
#se muestra el tipo de variable, la salida va a ser str
print(type(numero))
#se convierte la cadena a int
numero=int(numero)
#se muestra que ya cambio la variable, aun cuando el nombre de la variable es el mismo
print(type(numero))
#se declara una variable con meta
salida="el numero utilizado es {}"
#la salida va a ser la variable salida + la variable numero ya que para eso pusimos los{}
print(salida.format(numero))