run app: 

export/set FLASK_APP = application.py 
export FLASK_ENV = development
flask run


db.create_all()

relational database mapper, create objects and store data inside 

db.session.add(variable)
db.session.commit 

variable.query.all()