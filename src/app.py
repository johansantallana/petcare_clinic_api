from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

#sintaxis para cargar las variables de entorno
load_dotenv()

app = Flask(__name__)

#configuramos la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializar SQLAlchemy
db = SQLAlchemy(app)

#importar modelos despues de inicializar db
with app.app_context():
    from src.models.owner import Owner

#Ruta de pueba
@app.route('/')
def home():
    return jsonify({
        "message": "PetCare Clinic API",
        "status": "running"
    })
    
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)