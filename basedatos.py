import sqlite3

conexion = sqlite3.connect('controltvBD')#me conecto a la base de datos 
micursor = conexion.cursor()

micursor.execute("create table BDtv (code varchar(20),fecha varchar(50),\
    estado varchar(50),ubicacion varchar(50),\
    tipo varchar(50),modelo varchar(50),\
    cliente varchar(50), numorden varchar(50),\
    falla varchar(200),observaciones varchar(200),accesorios varchar(50))")

conexion.close()

