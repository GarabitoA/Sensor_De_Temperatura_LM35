"""
CUMPLIMIENTO REQUERIMIENTO 2
Crear un programa en Python que controle la temperatura del sensor y cuando el valor del sensor 
disminuya en -2 grados por la temperatura en su casa, se encienda un led de color rojo intermitente. 
En caso el sensor detecte dos grados más, se encienda un led de color azul constante. 
En caso contrario siempre se mantenga un led encendido del color que desee distinto a los anteriores.
"""

import tkinter
import serial,time
from tkinter import *
import pyfirmata #para uso del digitalwrite

arduino = serial.Serial("COM5",9600)
time.sleep(2)


#Cunplimiento requerimiento 1
print(" ------- TEMPERATURA ACTUAL -------")
while 1:
    lectura = arduino.readline().decode() #capturo datos del puerto serial en arduino ya convertidos a float
    temperatura = float(lectura)
    print(temperatura)
    if temperatura < 1.0:
        print("Mucho frio - Encendiendo LED  ROJO INTERMITENTE")
    elif temperatura >= 2.0 and temperatura < 3.0:
        print("Se detectaron 2 grados mas - Encendiendo LED AMARILLO")
    else:
        print("Temperatura normal")
    time.sleep(0.3)
