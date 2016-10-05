import sqlite3
tabla = sqlite3.connect("personas.db")
tabla.execute("CREATE TABLE Persona (id integer primary key autoincrement, nombre text, apellido text, edad integer)")
#tabla.execute( "INSERT INTO Persona()")

tabla.commit()
tabla.close()