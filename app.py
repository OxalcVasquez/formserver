from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        apellidos = request.form['apellidos']
        nombres = request.form['nombres']
        email = request.form['email']
        password = request.form['password']

	    # Establecer conexión a la base de datos
        connection = psycopg2.connect(
          user='postgres',
          password='',
          host='localhost',
         database='usuarios'
        )

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

# Insertar los datos en la tabla de usuarios
        query = "INSERT INTO usuarios (username, apellidos, nombres, email,password) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (username, apellidos, nombres, email,password))

# Confirmar los cambios en la base de datos
        connection.commit()

# Cerrar cursor y conexión
        cursor.close()
        connection.close()



        # Aquí puedes realizar las operaciones necesarias con los datos recibidos
        # como almacenarlos en una base de datos, enviar un correo, etc.

        return '¡Registro exitoso!'

    # Si la solicitud es GET, mostrar el formulario
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
