from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Characters(db.Model):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    specie = db.Column(db.String(250), nullable=False)
    genre = db.Column(db.String(250), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

class Starships(db.Model):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250))
    image = db.Column(db.String(250))

class Characters_Starships(db.Model):
    __tablename__ = 'characters_starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship(Character)
    starship_id = db.Column(db.Integer, db.ForeignKey('starship.id'))

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.Float, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(250))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }