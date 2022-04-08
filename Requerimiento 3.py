"""
CUMPLIMIENTO DEL REQUERIMIENTO 3
Realice un programa en Python que cuando el sensor de temperatura 
presente una media de +2 grados, mayor a la temperatura de su casa en pantalla, 
se muestre una imagen de Panic!. (color rojo y negro intermitente).
"""

from threading import current_thread
import tkinter
import serial,time
from tkinter import *
import pyfirmata #para uso del digitalwrite

arduino = serial.Serial("COM5",9600)
time.sleep(2)

current_temp = 27.0

#Cunplimiento requerimiento 1
print(" ------- TEMPERATURA ACTUAL -------")
while 1:
    lectura = arduino.readline().decode() #capturo datos del puerto serial en arduino ya convertidos a float
    tempe = float(lectura)
    print(tempe)
    if tempe >= current_temp:
        print("Se registro dos grados más a la temperatura normal - ¡CALOR!")
        ventana = Tk() #creando ventana que contendra nuestra imagen
        ventana.title("REGISTRO DE CALOR EN EL SENSOR LM35")
        ventana.configure(background='black')
        ventana.geometry('500x500')
        ventana.resizable(width=False, height=False)#El usuario no puede modificar el tamaño de la ventana
        img = tkinter.PhotoImage(file="panic.png") #Abriendo la imagen guardada en el mismo lugar del proyecto
        lbl_img = tkinter.Label(ventana,image = img) #creando etiqueta
        lbl_img.pack() #para mostrarlo mostramos el .pack
        ventana.mainloop()
    time.sleep(0.1)