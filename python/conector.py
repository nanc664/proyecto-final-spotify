#ARCHIVO PYTHON CONECTOR CON SQL
import mysql.connector

conx={
    "host":"localhost",
    "user":"root",
    "password":"Estudiante2025",
    "database":"colegio_db", #Cambien esto por el nombre de su propiabase de datos
    "port":"3307"
    }

conexion = mysql.connector.connect(**conx) #Esta variable (que contiene el comando de conexión del módulo mysql.connector) me permite conectar con la base de datos
cursor =conexion.cursor() #esta variable (que contiene el comando de comunicación del módulo mysql.connector) me permite consultar, escribiry editar la base de datos

print("conexion exitosa")






