# pip3 install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='abundancia1977',
  database='prueba'
)
 
cursor = mydb.cursor()

cursor.execute('select * from Usuarios ')
sql = 'insert into usuarios (email, username, edad) values (%s, %s, %s)'  
values = ('micorreo@correo.co.nz', 'nombreusuario', 25)
#cursor.execute(sql, values)
resultado = cursor.fetchall()
print(resultado)