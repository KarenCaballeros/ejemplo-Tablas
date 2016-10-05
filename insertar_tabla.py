import sqlite3
tabla = sqlite3.connect("personas.db")
tabla.execute( "INSERT INTO Persona(nombre, apellido, edad) VALUES('Ana', 'Caballeros', 16)")
tabla.execute( "INSERT INTO Persona(nombre, apellido, edad) VALUES('Willi', 'Rosal', 17)")
tabla.execute( "INSERT INTO Persona(nombre, apellido, edad) VALUES('Karla', 'Herrarte', 15)")
tabla.execute( "INSERT INTO Persona(nombre, apellido, edad) VALUES('Daniel', 'Perez', 20)")
tabla.execute( "INSERT INTO Persona(nombre, apellido, edad) VALUES('David', 'Aguirre', 18)")

tabla.commit()
tabla.close()