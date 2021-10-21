from flask import Flask
app= Flask(__name__)
from flask_sqlalchemy import SQLAlchemy



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'

@app.route('/')
def index():
    return 'hello'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks[]
        drink_data = {'name': Drink.name, 'description': Drink.description}

        output.append(drink_data)

    return{
        "drinks": output
    }


@app.route('/')
def get_drink(id):
    drink= Drink.query.get_or_404(id)
    return jsonify()