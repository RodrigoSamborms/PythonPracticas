#primero importe las librerias
import numpy as np
import matplotlib.pyplot as plt

#definimos una funcion, para este ejemplo tenemos una variable y tres constantes
def f(x,a,b,c):
    return a*x**2+b*x+c

xlist = np.linspace(-10,10,num=1000) #definimos una lista de 1000 puntos en el intervalo -10 a 10

ylist = f(xlist,3,1,4) #llamamos a la función evaluando los valores de la lista creada y con las constantes dadas

plt.figure(num=0, dpi=120) #definimos el plano donde mostraremos nuestras funciónes
plt.plot(xlist,ylist, label = "f(x)")#graficamos los puntos obtenidos anteriormente xlist=calculados automaticamente
                    #ylist= calculados por evaluar la función en esos puntos



#plt.plot(xlist,ylist**(1/2),'--',label = r"f(x)$^(0.5)$")

plt.plot(xlist,ylist**(1/2),'--',label = r"f(x)**(1/2)")

plt.title("Grafica de Ejemplo")
plt.xlabel("Distancia / mts") #agrega la etiqueta al eje X
plt.ylabel("Altura / mts")  #agrega la etiqueta al eje Y
plt.legend()

plt.show()#Esta función muestra la figura 

