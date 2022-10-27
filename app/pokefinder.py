import requests as req


def PokeFinder(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = req.get(url)
    if response.ok:
        data = response.json()
        poke_dict = {}
        poke_attributes = data
        poke_dict= {
            'poke_name': poke_attributes['name'],
            'poke_ability': poke_attributes['abilities'][0]['ability']['name'],
            'base_hp': poke_attributes['stats'][0]['base_stat'],
            'base_att': poke_attributes['stats'][1]['base_stat'],
            'base_def': poke_attributes['stats'][2]['base_stat'],
            'sprite': poke_attributes['sprites']['front_default']
        }        
        return poke_dict
    return "Error. That is not a POKEMON!"