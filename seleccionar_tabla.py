import sqlite3
tabla = sqlite3.connect("personas.db")

resultado = tabla.execute("SELECT * FROM Persona")

for i in resultado:
	print(i)

tabla.commit()
tabla.close()