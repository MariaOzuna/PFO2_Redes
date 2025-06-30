
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Servidor funcionando correctamente"


# Crear la base de datos si no existe
def crear_tabla():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Ruta para registrar usuarios
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = generate_password_hash(data.get('contraseña'))

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña))
        conn.commit()
        return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201
    except:
        return jsonify({'error': 'Usuario ya existe'}), 400
    finally:
        conn.close()

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and check_password_hash(resultado[0], contraseña):
        return jsonify({'mensaje': 'Login exitoso'})
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

# Ruta de bienvenida
@app.route('/tareas', methods=['GET'])
def tareas():
    return '''
    <html>
        <head><title>Bienvenido</title></head>
        <body><h1>¡Bienvenido al gestor de tareas!</h1></body>
    </html>
    '''

if __name__ == '__main__':
    crear_tabla()
    app.run(debug=True)
