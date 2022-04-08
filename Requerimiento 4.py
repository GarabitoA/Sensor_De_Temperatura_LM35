"""
CUMPLIMIENTO DE REQUERIMIENTO 4
Realice un programa que grafique la temperatura durante 5 horas de su casa.
Esta gráfica debe mostrar la información clara de manera que se presenten
los picos de temperatura y los momentos en que baja.


"""

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

comunicacion = serial.Serial("COM5",9600)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xdatos, ydatos = [], []

while True:
    if(comunicacion.inWaiting()>0):
        def animate(i,xdatos,ydatos):
            datos = comunicacion.readline()
            datos = float(datos)    
            xdatos.append(i)
            ydatos.append(datos)
            print(datos)
            #ax.clear()
            ax.plot(xdatos,ydatos)

        ani = animation.FuncAnimation(fig,animate, fargs=(xdatos,ydatos))
        plt.show()
