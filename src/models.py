from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    #relationship('Favorite', backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass":self.mass,
            "hair_color":self.hair_color,
            "eye_color": self.eye_color,
            "skin_color":self.skin_color,
            "birth_year": self.birth_year,
            "gender": self.gender


            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    climate = db.Column(db.String(250), nullable=True)
    population = db.Column(db.Integer, nullable=True)
    orbital_period  = db.Column(db.Integer, nullable=True)
    rotation_period = db.Column(db.Integer, nullable=True)
    diameter = db.Column(db.Integer, nullable=True)
    # favoritos = db.relationship ('favoritos', backref= 'planets', lazy=True)
    def __repr__(self):
        return '<planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "climate": self.climate,
            "population": self.population, 
            "orbital_period": self.orbital_period,  
            "rotation_period": self.rotation_period,
            "diameter": self.diameter
            # do not serialize the password, its a security breach
        }
    
class Favorito(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(250), nullable=False)
    # type= db.Column(db.Integer)
    characters_id= db.Column(db.Integer, db.ForeignKey('characters.id'),nullable=True)
    planets_id= db.Column(db.Integer, db.ForeignKey('planets.id'),nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    def __repr__(self):
        return '<favoritos %r>' % self.id

    def serialize(self):
        character_query= Character.query.filter_by(id= self.characters_id).first()

        if character_query is None:
          character_resultado=  None
        else:
          character_resultado= character_query.serialize()['name']

        planet_query= Planet.query.filter_by(id= self.planets_id).first()

        if planet_query is None:
          planet_resultado=  None
        else:
          planet_resultado= planet_query.serialize()['name']
        

        return {
            "id": self.id,
            "characters": character_resultado,
            "planets": planet_resultado,
            "user_id": self.user_id
            # do not serialize the password, its a security breach // planet_query.serialize()['name'] // character_query.serialize()['name']
        }