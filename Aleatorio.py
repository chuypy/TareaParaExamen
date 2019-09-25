#Importamos librerias que ya viene al momento de instalar python
import random

#delacaramos una variable float con un valor de 10.5
numero1=float(10.5)

#hacemos una funcion  que declare otra variable float con un valor random que es generado
#por la libreria random y lo sumamos para que el resultado sea la varaiable numero1+numero2 
#siempre sera un resultado diferente

def funAleatorio():
    numero2=float(random.randrange(1,10))
    mensaje="la suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
#llamamos a la funcion
funAleatorio()