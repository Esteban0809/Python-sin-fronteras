from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

# __name__ es el nombre del archivo en este caso es holamundo
app = Flask(__name__)

midb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='abundancia1977',
  database='prueba'
)

# Vamos a cambiar la configuracion por defecto del cursor
# ya que con el fetall esto trae una lista de tuplas y para 
# acceder a sus valores hay que hacerlo por indice, lo vamos 
# a cambiar para poder acceder a su nombre y no a su indice 
# dictionary=True
cursor = midb.cursor(dictionary=True)

# curl -X GET http://localhost:5000
@app.route('/')
def index():
  return '<h1>Cabrones de mierda hijos de perra</h1>'

# Por defecto es GET
# GET, POST, DELETE
# PUT(actualizar un recurso completo), 
# PATCH(actualizar parcialmente un recurso)
# Forzar para que sea un entero <int:post_id>
# curl -X GET http://localhost:5000/post/1
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
  if request.method == 'GET':
    return 'El id del post es:' + post_id
  else:
    return 'Este es otro metodo y no GET '

# @app.route('/post/<post_id>', methods=['POST'])
# def savePost(post_id):
#   return 'El id del post es: ' + post_id

@app.route('/user/<user>')
def user(user):
  return 'Usuario ingresado: ' + user

# curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000 
@app.route('/test', methods=['POST'])
def test():
  # Formar URLs url_for
  nombreFuncion = 'index'
  print('== url_for', url_for(nombreFuncion))
  nombreFuncion2 = 'post'
  print('== url_for', url_for(nombreFuncion2, post_id=2))
  print('== form', request.form)
  print('== form', request.form['llave1'])
  print('== form', request.form['llave2'])
  return 'Test'

# curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/test-redirect
@app.route('/test-redirect', methods=['POST', 'GET'])
def testRedirect():
  nombreFuncion = 'post'
  path = url_for(nombreFuncion, post_id=2)
  return redirect(path)

# Abortar peticioón
@app.route('/test-abort', methods=['POST', 'GET'])
def testAbort():
  # abort(401)
  abort(403)
  nombreFuncion = 'post'
  path = url_for(nombreFuncion, post_id=2)
  return redirect(path)


# Redireccionar Templates HTML
# Flask buscara una carpeta llamada templates
@app.route('/test-template', methods=['GET'])
def testTemplate():
  return render_template('template.html')

# Retornar JSON (Diccionario)
@app.route('/test-json')
def testJson():
  return {
    "username": "Jesus Camacaro",
    "email": "root@mail.com"
  }

# Extencion
# Redireccionar Templates HTML
# Flask buscara una carpeta llamada templates
@app.route('/home', methods=['GET'])
def home():
  return render_template('home.html', mensaje='Hola Mundo')


@app.route('/db', methods=['GET'])
def getUsers():
  cursor.execute('select * from Usuarios')
  usuarios = cursor.fetchall()
  #  Esto devuelve una lista que contiene tuplas
  # [(1, 'chanchito@faliz.com', 'fchanchito', None)]

  # con la configuracion que hicimos en cursor ahora retorna un diccionario
  # una lista de diccionario
  # [{'id': 1, 'correo': 'chanchito@faliz.com', 'usuario': 'fchanchito', 'edad': None}]
  return render_template('usuarios.html', usuarios=usuarios)


@app.route('/crear-usuario', methods=['GET', 'POST'])
def createUser():
  if request.method == 'POST':
    usuario = request.form['usuarios']
    edad = request.form['edad']
    correo = request.form['email']
    sql = 'insert into Usuarios (username, email, edad) values (%s, %s, %s)'
    values = (username, email, edad)
    cursor.execute(sql, values)
    midb.commit()
    nombreFuncion = 'getUsers'
    path = url_for(nombreFuncion)
    return redirect(path)

  return render_template('form-user.html')
