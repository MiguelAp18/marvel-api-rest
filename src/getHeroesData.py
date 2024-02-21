import requests
import ssl

url = 'https://gateway.marvel.com/v1/public/characters?ts=1&apikey=f20558c4da7a382a1fddf12ef87b393d&hash=bce25f7f89695f829929c345f5850c86'

heroes_list = []

class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        kwargs['ssl_context'] = ctx
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

def heroesData():
    session = requests.session()
    session.mount('https://', TLSAdapter())
    res = session.get(url)
    all_heroes = res.json()['data']['results']

    for i in all_heroes:
        name = i['name']
        description = i['description']
        comics_available = i['comics']['available']
        series_available = i['series']['available']

        heroes_dictionary = {
            'name': name, 
            'description': description,
            'comics_available': comics_available,
            'series_available': series_available
        }

        heroes_list.append(heroes_dictionary)
    
    return heroes_list
                             