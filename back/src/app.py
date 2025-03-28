from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
# Habilitar CORS para todas las rutas
CORS(app)

# Configuración de Flask-PyMongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
# Inicializar Flask-PyMongo
mongo = PyMongo(app)


#enlaces
@app.route('/createBook', methods=['POST'])
def createBook():
    pass
@app.route('/listBook/<id>', methods=['GET'])
def listBook():
    pass

@app.route('/updateBook/<id>', methods=['PUT'])
def updateBook(id):
    pass

@app.route('/deleteBook/<id>', methods=['DELETE'])
def deleteBook(id):
    pass

#si es la aplicación principal para correr en el servidor
if __name__ == "__main__":
    app.run(debug=True)
