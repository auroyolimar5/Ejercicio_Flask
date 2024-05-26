from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para flash messages

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb://usuario:example@localhost:27017/ejericio1"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    # Insertar el usuario en la base de datos
    mongo.db.users.insert_one({'name': name})
    return render_template('greeting.html', name=name)


@app.route('/users')
def users():
    # Obtener todos los usuarios de la base de datos
    users = mongo.db.users.find()
    return render_template('users.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validación básica
        if not name or not email or not password:
            flash('Todos los campos son obligatorios.')
            return redirect(url_for('register'))

        # Hash de la contraseña
        hashed_password = generate_password_hash(password, method='pbkdf2')

        # Insertar el usuario en la base de datos
        mongo.db.users.insert_one({
            'name': name,
            'email': email,
            'password': hashed_password
        })

        flash('Usuario creado exitosamente!')
        return redirect(url_for('users'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
