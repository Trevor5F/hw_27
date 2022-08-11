from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  text

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'postgresql://db_user:db_user:db_password'

db = SQLAlchemy

@app.route('/')
def index():
    test = None
    test = db.session.execute(text('SELECT "TEST"')).scalar()
    return f'It`s alive: {test}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)