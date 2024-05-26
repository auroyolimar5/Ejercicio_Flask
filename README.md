# Ejercicio Flask 1

Primer ejercicio sencillo de programación en Python usando Flask, de una pequeña aplicación web que tenga las siguientes funcionalidades:

- Una página de inicio que muestra un formulario donde el usuario puede ingresar su nombre.
- Cuando el usuario envía el formulario, se muestra una página de saludo con su nombre.

## Pasos para crear la aplicación:

### Crear el entorno virtual de Python:

```sh
python -m venv venv
```
### Activar el entorno virtual:
- En windows:
```bash
.\venv\Scripts\activate
```
- En linux:
```bash
source /venv/bin/activate
```

### Instalar librerias: 

Instalar una a una:

```sh
pip install flask
```
O instalar todas desde el archivo de `requirements.txt`:

```sh
pip install -r requirements.txt
```

Crear la estructura del proyecto:

```markdown
Ejercicio_Flask/
├── app.py
├── templates/
│   ├── index.html
│   ├── greeting.html
│   └── users.html
└── static/
    └── styles.css
```
Código para app.py:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

Código para templates/index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Saludo</title>
</head>
<body>
    <h1>Introduce tu nombre</h1>
    <form action="/greet" method="POST">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```
Código para templates/greeting.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saludo</title>
</head>
<body>
    <h1>Hola, {{ name }}!</h1>
    <a href="/">Volver</a>
</body>
</html>
```
## Descripción del flujo de trabajo:
##### 1. Página de Inicio (`index.html`):

- Presenta un formulario donde el usuario puede ingresar su nombre.
- El formulario envía una solicitud POST a la ruta /greet cuando se envía.

##### 2. Ruta `/greet`:

- Recibe el nombre del usuario desde el formulario.
- Renderiza la plantilla greeting.html pasando el nombre como parámetro.

##### 3. Página de Saludo (`greeting.html`):

- Muestra un mensaje personalizado con el nombre del usuario.
- Incluye un enlace para volver a la página de inicio.

## Ejecución de la Aplicación:
Para ejecutar la aplicación, navega al directorio del proyecto en tu terminal y ejecuta:

```sh
python app.py
```
Abre tu navegador web y navega a http://127.0.0.1:5000/ para ver la aplicación en acción.