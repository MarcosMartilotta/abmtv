#!/usr/bin/env python
# -*- coding: utf-8 -*-

#librerías
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import sqlite3


def aleatorio():
    codigo = random.randint(1,9999)
    return codigo

def agrega():
#falta agregar que te muestre el código de autenticación
    a = aleatorio()
    b = fehcabox.get()
    c = estado.get()
    d = ubicacion.get()
    e = tipo.get()
    f = boxmodelo.get()
    g = boxcliente.get()
    h = numordenbox.get()
    i = boxfalla.get()
    j = boxobs.get()
    k = boxaccesorios.get()

    fehcabox.delete(0,tk.END)
    estado.set("")
    ubicacion.set("")
    tipo.set("")
    boxmodelo.delete(0,tk.END)
    boxcliente.delete(0,tk.END)
    numordenbox.delete(0,tk.END)
    boxfalla.delete(0,tk.END)    
    boxobs.delete(0,tk.END)
    boxaccesorios.delete(0,tk.END)
     
    nuevoIngreso = [(a,b,c,d,e,f,g,h,i,j,k)] 

    conexion = sqlite3.connect("controltvBD")#me conecto a la base de datos 
    micursor = conexion.cursor() 

    micursor.executemany("insert into BDtv values (?,?,?,?,?,?,?,?,?,?,?)", nuevoIngreso)
    conexion.commit()
    conexion.close()

    messagebox.showinfo('Nuevo código', a)

def borra(): #esta funcion borraría algun registro completo
    codigo = codigobox.get()
    codigobox.delete(0,tk.END)

    conexion = sqlite3.connect("controltvBD")#me conecto a la base de datos 
    micursor = conexion.cursor() 

    micursor.execute("DELETE FROM BDtv where code = ?",[codigo])


    conexion.commit()
    conexion.close()


def busqueda(): 
    codigo = codigobox.get()
    codigobox.delete(0,tk.END)
    dia = fehcabox.get()
    fehcabox.delete(0,tk.END)

    conexion = sqlite3.connect("controltvBD")#me conecto a la base de datos 
    micursor = conexion.cursor() 

    for row in micursor.execute("SELECT * FROM BDtv where code = ? and fecha =?",[codigo,fecha]):
        print(row)
    
    conexion.commit()
    conexion.close()



############main#########################

ventana = tk.Tk()
ventana.title("ControlTv")
ventana.config(width = 700, height= 800)

############boxes########################

boxcliente = tk.Entry()
boxcliente.place(x = 20, y = 45)
boxmodelo = tk.Entry()
boxmodelo.place(x = 20, y = 95)
boxaccesorios = tk.Entry()
boxaccesorios.place(x = 20, y = 145)
boxfalla = tk.Entry()
boxfalla.place(x = 20, y = 195)
boxobs = tk.Entry()
boxobs.place(x = 20, y = 245)
date = time.asctime()
fehcabox = tk.Entry()
fehcabox.insert(0, date[4:7] + " " + date[8:10] + " " + date[-4:])
fehcabox.place(x = 550, y = 20)
numordenbox = tk.Entry()
numordenbox.place(x = 20, y = 445)
codigobox = tk.Entry()
codigobox.place(x = 550, y = 70)

###########desplegables#################

tipo = ttk.Combobox(values = ["TV", "MAIN", "TCON", "FUENTE", "INVERTER", "TIRA LED", "OTRO"])
tipo.place(x = 20, y = 295)
estado = ttk.Combobox(values = ["Reparado", "Entregado", "A reparar", "Visto", "Devolucion", "Espera respuesto"])
estado.place(x = 20, y = 345)
ubicacion = ttk.Combobox(values = ["Entrada", "Federico", "Patio", "Marcos", "Cocina"])
ubicacion.place(x = 20, y = 395)

##########textos/labels#####################

textcliente = tk.Label(text = "Cliente:")
textcliente.place(x = 20, y = 20)
textmodelo = tk.Label(text = "Modelo: ")
textmodelo.place(x = 20, y = 70)
textaccesorios = tk.Label(text = "Accesorios: ")
textaccesorios.place(x = 20, y = 120)
textfalla = tk.Label(text = "Falla: ")
textfalla.place(x = 20, y = 170)
textobs = tk.Label(text = "Obeservaciones: ")
textobs.place(x = 20, y = 220)
texttipo = tk.Label(text = "Tipo: ")
texttipo.place(x = 20, y = 270)
fecha = tk.Label(text = "Fecha: ")
fecha.place(x = 500, y = 20)
textestado = tk.Label(text = "Estado: ")
textestado.place(x = 20, y = 320)
textubicacion = tk.Label(text = "Ubicacion: ")
textubicacion.place(x = 20, y = 370)
textnumorden = tk.Label(text = "Numero de orden: ")
textnumorden.place(x = 20, y = 420)

#############botones#########################

agregar = tk.Button(text = "Agregar", command = agrega)
agregar.place(x = 20, y = 500)
borrar = tk.Button(text = "Borrar", command = borra)
borrar.place(x = 500 ,y = 120)
buscar = tk.Button(text = "Buscar", command = busqueda)
buscar.place(x = 500, y = 70)


ventana.mainloop()
