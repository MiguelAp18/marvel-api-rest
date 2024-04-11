from flask import Blueprint, jsonify, request
import uuid

# Models
from models.hero_model import hero_model

# Entities
from models.entities.hero import Hero

# Heroes Data
from getHeroesData import heroesData

main = Blueprint('hero_blueprint', __name__)

@main.route('/')
def getHeroes():
    try:
        heroes = hero_model.get_heroes()
        return jsonify(heroes)
    except Exception as ex:
        return jsonify({
            'message': str(Exception(ex))
        }), 500
    
@main.route('/<id>')
def getHero(id):
    try:
        hero = hero_model.get_hero(id)
        if hero != None:
            return jsonify(hero)
        else:
            return jsonify({
                'message': 'Record not found'
            }), 404
    except Exception as ex:
        return jsonify({
            'message': str(Exception(ex))
        }), 500
    
@main.route('/add', methods=['POST'])
def addHero():
    try:    

        id = uuid.uuid4()
        name = request.json['name']
        description = request.json['description']
        comics_available = int(request.json['comics_available'])
        series_available = int(request.json['series_available'])

        hero = Hero(str(id), name, description, comics_available, series_available)          
        affected_rows = hero_model.add_hero(hero)
        
        if affected_rows != 0:
            return jsonify({'record inserted': affected_rows})
        else:
            return jsonify({
                'message': 'Error on insert'
            }), 500
        
    except Exception as ex:
        return jsonify({
            'message': str(Exception(ex))
        }), 500
    
@main.route('/update/<id>', methods=['PUT'])
def updateHero(id):
    try:
        
        name = request.json['name']
        description = request.json['description']
        comics_available = int(request.json['comics_available'])
        series_available = int(request.json['series_available'])
        hero = Hero(id, name, description, series_available, comics_available)

        affected_rows = hero_model.update_hero(hero)

        if affected_rows != 0:
            return jsonify({'records updated': affected_rows})
        else:
            return jsonify({
                'message': 'Record not found'
            }), 404
        
    except Exception as ex:
        return jsonify({
            'message': str(Exception(ex))
        }), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def deleteHero(id):
    try:
        hero = Hero(id)

        affected_rows = hero_model.delete_hero(hero)

        if affected_rows != 0:
            return jsonify({'records deleted': affected_rows})
        else:
            return jsonify({
                'message': 'Record not found'
            }), 404
        
    except Exception as ex:
        return jsonify({
            'message': str(Exception(ex))
        }), 500
    
@main.route('/upload', methods=['POST'])
def uploadHeroes():
    try:    

        heroes_list = heroesData()

        hero = ''
        id = ''
        affected_rows = 0

        for data in heroes_list:

            id = uuid.uuid4()
            name = data['name']
            description = data['description']
            comics_available = int(data['comics_available'])
            series_available = int(data['series_available'])

            hero = Hero(str(id), name, description, comics_available, series_available)          
            affected_rows += hero_model.add_hero(hero)
        
        if affected_rows != 0:
            return jsonify({'records uploaded': affected_rows})
        else:
            return jsonify({
                'message': 'Error on insert'
            }), 500
        
    except Exception as ex:
        return jsonify({
            'message': str(Exception(ex))
        }), 500