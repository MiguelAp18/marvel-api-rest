from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes import hero

app = Flask(__name__)

CORS(app, resources={'*': {'origins': 'http://localhost:3000'}})

def pageNotFound(error):
    return '<h1> Not found page </h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(hero.main, url_prefix='/api/heroes')

    #Error handling
    app.register_error_handler(404, pageNotFound)
    app.run()