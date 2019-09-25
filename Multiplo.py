numero=int(input("dame un numero entero: "))
#se almacenan valores booleanos la evaluacion de residuales. Si el residual es cero, quiere decir que el numero es multiplo

esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

#cuando se usa and, se resuelve por erdadero si todas las condiciones son verdaderas, cuando e usa or, se resuelvepor verdero
#si al menos una condicion es verdadera. los parentecis le dicen a python
#las primeras dos condiciones son jntas y la tercera es independiente 
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("es correcto")

else:
    print("incorrecto")