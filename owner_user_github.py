# se genera soliciud de importación para generar conexión a la BD

import mysql.connector

# se genera conexión a la BD general

mydb = mysql.connector.connect(host='localhost', user='root', passwd='')

# Se inicia variable de ejecución mycursor

mycursor = mydb.cursor()

# se genera adición a una nueva BD

mycursor.execute("CREATE DATABASE IF NOT EXISTS dblist")

# se genera conexión a la bd generada en el punto anterior DBLIST

mydb = mysql.connector.connect(host='localhost', user='root', passwd='', db="dblist")

# Se inicia variable de ejecución mycursor

mycursor = mydb.cursor()

# se genera adición a nueva tabla donde se alojara información denominada userowner

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS userowner (row_id INT (100), dn_name VARCHAR(9) NOT NULL, classificationconfidentiality VARCHAR(6) NOT NULL, classificationintegrity VARCHAR(6) NOT NULL, classificationavailability VARCHAR(6) NOT NULL, ownername VARCHAR(18) NOT NULL, owneruid VARCHAR(11) NOT NULL PRIMARY KEY, user_state VARCHAR(11) NOT NULL,  owneremail VARCHAR(36) NOT NULL, time_stamp VARCHAR(26) NOT NULL, email_manager VARCHAR(30) NOT NULL) ")

# Se inicia variable de ejecución mycursor

mycursor = mydb.cursor()

# se genera adición a nueva tabla donde se alojara información de logs denominada log

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS log (owneruid VARCHAR(100) NOT NULL, classificationconfidentiality VARCHAR(100) NOT NULL ,classificationintegrity VARCHAR(100) NOT NULL, classificationavailability VARCHAR(100) NOT NULL, email_manager VARCHAR(100)) ")

# Se inicia variable de ejecución mycursor

mycursor = mydb.cursor()

# se genera inserción de datos a la tabla owneruser

sql = "INSERT INTO userowner (row_id, dn_name, classificationconfidentiality, classificationintegrity, classificationavailability, ownername, owneruid, user_state, owneremail, time_stamp, email_manager) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = [
    ('1', 'user', 'low', 'high', 'medium', 'Enzo Trossero', 'etrossero', 'activo', 'N/A', '2018-11-28 17:10:07.414345', 'N/A'),
    ('2', 'items', 'medium', 'low', 'N/A', 'Daniel Bertoni', 'dbertoni', 'activo', 'N/A', '2018-11-28 17:10:07.414345','N/A'),
    ('3', 'locations', 'high', 'high', 'low', 'Ricardo Bochini', 'rbochini', 'activo', 'N/A', '2018-11-28 17:10:07.414345', 'N/A'),
    ('4', 'sellers', 'low', 'medium', 'medium', 'Daniel Garnero', 'dgarnero', 'activo', 'N/A', '2018-11-28 17:10:07.414345', 'N/A'),
    ('5', 'sellers', 'low', 'low', 'medium', 'José Pastoriza', 'jopastoriza', 'activo', 'N/A', '2018-11-28 17:10:07.414345', 'N/A'),
    ('6', 'orders', 'high', 'high', 'medium', 'Luis Alberto Islas', 'laislas', 'activo', 'N/A', '2018-11-28 17:10:07.414345', 'N/A'),
    ('7', 'questions', 'low', 'low', 'low', 'Albeiro Usuriaga', 'ausuriaga', 'Inactivo', 'N/A', '2018-11-28 17:10:07.414345', 'N/A')
]
# se enuncian las variables sql, val

mycursor.executemany(sql, val)

mydb.commit()

# se genera mensaje de confirmación de datos insertados

print(mycursor.rowcount, "was inserted.")

# Disconnecting from the database
mydb.close()