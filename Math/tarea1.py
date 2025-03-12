#programa que cualcula las señales continuas en el tiempo de las siguentes funciones
#defimos pi = math.pi = 3.14.1592653589793
#Tomando en cuenta que w = 2*pi*frec 
#   f(t)=A*sin(w*t + o)     =  A*sin((2*pi*frec)*t + o) 
#   g(t)=A*sin(2*w*t)       =  A*sin(2*(2*pi*frec)*t)
#   h(t)=A*sin(3*w*t)       =  A*sin(3*(2*pi*frec)*t)
#importamos las librerias   
import matplotlib.pyplot as plt
import numpy as np
import math

#definimos las etiquetas de las funciones
f1 = "f(t)=A*sin(w*t + o)" #+ "= A*sin((2*pi*frec)*t + o)" 
g1 = "A*sin(2*w*t)" #+     " =  A*sin(2*(2*pi*frec)*t)"
h1 = "A*sin(3*w*t)" #+     " =  A*sin(3*(2*pi*frec)*t)"

#calculamos un rango de datos para usar con nuestras funciones
pi = math.pi
x = np.arange(0, 4*np.pi, 0.5)

#definimos las funciones
def f(x, A = 1, frec = 1, o = 0): #primero las variables y despues las constantes
    return  A*np.sin(((2*pi*frec)*x) + o) 

def g(x, A = 1, frec = 1, o = 0):
    return A*np.sin(2*(2*pi*frec)*x)

def h(x, A = 1, frec = 1, o = 0):
    return A*np.sin(3*(2*pi*frec)*x)

rango = [ 2, 1]
Amplitud = 1/2
Frecuencia = 2
Desplazamiento = 1

#print (rango[1])


y1 = f(x, Amplitud , 1, 0)  #funcion seno con Amplitud=1, frec=1Hz, desplazamiento o= 0 (funcion seno simple)
y2 = g(x, 1, Frecuencia, 0)  #funcion seno con Amplitud=1, frec=1Hz, desplazamiento o= 0 (funcion seno simple)
y3 = h(x, 1, 1, Desplazamiento)  #funcion seno con Amplitud=1, frec=1Hz, desplazamiento o= 0 (funcion seno simple)



plt.figure(num = 0, dpi = 120)


plt.plot(x, y1, marker = '+', label = f1 ,linestyle = "-.") #graficamos la funcion
plt.plot(x, y2, marker = 'o', label = g1 ,linestyle = "-") #graficamos la funcion
plt.plot(x, y3, marker = '*', label = h1 ,linestyle = ":") #graficamos la funcion


plt.legend()
plt.show()
