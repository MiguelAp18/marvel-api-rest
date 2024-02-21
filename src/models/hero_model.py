from database.db import get_connection
from .entities.hero import Hero

class hero_model():

    @classmethod
    def get_heroes(self):
        try:
            connection = get_connection()
            heroes = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, description, comics_available, series_available FROM hero ORDER BY name ASC")
                result_set = cursor.fetchall()

                for row in result_set:
                    hero = Hero(row[0], row[1], row[2], row[3], row[4])
                    heroes.append(hero.to_json())

            connection.close()
            return heroes

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_hero(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, description, comics_available, series_available FROM hero WHERE id = %s", (id,))
                row = cursor.fetchone()

                hero = None
                if row != None:
                    hero = Hero(row[0], row[1], row[2], row[3], row[4])
                    hero = hero.to_json()

            connection.close()
            return hero

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_hero(self, hero):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO hero (id, name, description, comics_available, series_available)
                                VALUES (%s, %s, %s, %s, %s)""", (hero.id, hero.name, hero.description, hero.comics_available, hero.series_available))
                affected_rows = cursor.rowcount
                connection.commit()   

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_hero(self, hero):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE hero SET name = %s, description = %s, comics_available = %s, series_available = %s
                                WHERE id = %s""", (hero.name, hero.description, hero.comics_available, hero.series_available, hero.id))
                affected_rows = cursor.rowcount
                connection.commit()   

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_hero(self, hero):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM hero WHERE id = %s", (hero.id,))
                affected_rows = cursor.rowcount
                connection.commit()   

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)