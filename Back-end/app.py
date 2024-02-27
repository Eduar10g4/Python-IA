from models import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/api_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define tus modelos aquí

if __name__ == '_main_':
    # Importa tus modelos aquí para que SQLAlchemy pueda reconocerlos
    

    # Crea todas las tablas definidas en tus modelos
    db.create_all()

    # Ejecuta la aplicación Flask
    app.run(debug=True)