"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code



# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def getCharacters():
    json_text = jsonify('character')
    return json_text

@app.route('/characters/create', methods=['GET', 'POST'])
def createCharacters():
    if request.method == "POST":
        characters = Characters(
            id = request.get_json(force = True),
            name = request.get_json(force = True),
            specie = request.get_json(force = True),
            genre = request.get_json(force = True),
            planet_id = request.get_json(force = True)
        )
        db.session.add(characters)
        db.session.commit()
        return Characters

    return render_template("user/create.html")

@app.route('/characters/<int:character_id>', methods=['GET'])
def getCharacterById():
    json_text = jsonify('character_id')
    return json_text

@app.route('/starships', methods=['GET'])
def getStarships():
    json_text = jsonify('starship')
    return json_text

@app.route('/starships/<int:starship_id>', methods=['GET'])
def getStarshipById():
    json_text = jsonify('starship_id')
    return json_text

@app.route('/planets', methods=['GET'])
def getPlanets():
    json_text = jsonify('planet')
    return json_text

@app.route('/planets/<int:planet_id>', methods=['GET'])
def getPlanetById():
    json_text = jsonify('planet_id')
    return json_text

@app.route('/characters_starships', methods=['GET'])
def getCharactersStarships():
    json_text = jsonify('characters_starships')
    return json_text

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
