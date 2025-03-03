from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'useroot'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)


@app.route('/')
def Index():
    return 'Hello World'

@app.route('/add')
def add_contact():
    return 'Contact'

@app.route('/edit')
def edit_contact():
    return 'Edit Contact'

@app.route('/delete')
def delete_contact():
    return 'Delete Contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)