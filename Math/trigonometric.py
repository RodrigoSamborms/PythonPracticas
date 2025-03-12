#importamos las librerias
import matplotlib.pyplot as plt
import numpy as np

#t = [0, 30, 45, 60, 90] #Generamos una lista con los angulos que deseamos usar
#x = [i*(np.pi/18) for i in t] #Debemos convertir los angulos de la lista de Grados a Radianes
#t = np.linspace(-np.pi, np.pi)
t = np.arange(0, 4*np.pi, 0.5)

#plt.figure(num=0, dpi=120)#Si no definimos un area de trabajo, las funciones se presentan en una ventana con opciones
                            #Por default

#plt.plot(t,np.sin(x), marker = "+", label = "Seno")
#plt.plot(t,np.cos(x), marker = "^", label = "Coseno")

plt.plot(t,np.sin(t), marker = "+", label = "Seno", linestyle = "-.")#opción marker indica los puntos de los ejes
plt.plot(t,np.cos(t), marker = "^", label = "Coseno", linestyle = ":")#opción linestyle indica los demas 
                                                                    #puntos a graficar

#plt.xticks(t) #Este método ajusta los valores de X solo a los de la lista
plt.title("grafica de Seno y Coseno")
plt.xlabel("angulo en radianes")
plt.ylabel("Valores de Seno y Coseno")

plt.legend()
plt.show()

