class Hero():

    def __init__(self, id, name=None, description=None, comics_available=None, series_available=None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.comics_available = comics_available
        self.series_available = series_available

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'comics_available': self.comics_available,
            'series_available': self.series_available
        }