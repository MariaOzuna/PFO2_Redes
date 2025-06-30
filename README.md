# Proyecto PFO2 – Gestor de Tareas con API Flask y SQLite
Programación sobre Redes - IFTS 29
Autor: Ozuna, Maria Ofelia -- Docente: Germán Rios

--- 

Esta es una aplicación simple que permite:

✅ Registrar usuarios  
✅ Iniciar sesión  
✅ Ver una página de bienvenida  

Todo esto se maneja mediante una API creada con **Flask** y una base de datos **SQLite**.

---

##  Instrucciones para ejecutar el proyecto

### 1. Clonar o descargar el proyecto

> Si lo bajaste manualmente, asegurate de tener estos archivos:
- `servidor.py`
- `README.md`
- Las capturas de pantalla

---

### 2. Instalar Python y las dependencias necesarias
- Flask y Werkzeug se instalan desde la terminal. Ejecutá:

pip3 install flask werkzeug

---

### 3. Ejecutar el servidor
- Desde la terminal, dentro de la carpeta del proyecto, ejecutá:

python3 servidor.py

Si todo está bien, deberías ver:

 * Running on http://127.0.0.1:5000/

---

## ¿Cómo probar el proyecto?
# Registro de usuario

curl -X POST http://127.0.0.1:5000/registro \
  -H "Content-Type: application/json" \
  -d '{"usuario": "maria", "contraseña": "1234"}'

- Respuesta esperada:

{"mensaje": "Usuario registrado correctamente"}

---

## Login

curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"usuario": "maria", "contraseña": "1234"}'

- Respuesta esperada:

{"mensaje": "Login exitoso"}

---

## Página HTML de bienvenida

- Abrí el navegador y pegá:

http://127.0.0.1:5000/tareas

- Deberías ver un mensaje:
¡Bienvenido al gestor de tareas!

### Capturas de pantalla

- Registro exitoso



- Login exitoso



- Página HTML de bienvenida


### Respuestas Conceptuales

# ¿Por qué hashear contraseñas?

Hashear contraseñas es una medida de seguridad fundamental para proteger los datos de los usuarios.
Cuando un usuario se registra, escribe una contraseña. Si el sistema la guarda en texto plano (tal como fue escrita), cualquier persona que acceda a la base de datos —por accidente o por un ataque— podría ver esas contraseñas y usarlas maliciosamente.

En cambio, cuando se aplica una función de hash, esa contraseña se convierte en un conjunto de caracteres irreconocibles (como “$pbkdf2-sha256$29000$…”).
Lo importante es que este proceso no es reversible: no se puede obtener la contraseña original a partir del hash.

Además:
Cada vez que se hashea la misma contraseña, se genera un resultado distinto (gracias a algo llamado “salt”).
El sistema no compara la contraseña directa, sino el resultado del hash generado al ingresar y el que está guardado.

# Ventajas de usar SQLite en este proyecto

SQLite es una base de datos muy liviana que no necesita servidores externos ni configuraciones complicadas. Es ideal para comenzar a trabajar con datos y aprender cómo funciona una base real.
- Fácil de usar: Podés empezar a guardar y consultar datos sin tener que instalar software adicional ni configurar un servidor.
- Portátil: Todos los datos se guardan en un solo archivo .db que podés copiar o mover fácilmente.
- Rápida y suficiente para aplicaciones pequeñas como esta.
- Integrada con Python: Se puede usar con la librería sqlite3, que ya viene incluida con Python.