from utils.pokemonDB import PokemonDB
from utils.pokemon import Pokemon
import pandas as pd

def get_abilidades(row: pd.Series) -> list[str]:
    abilidade:list = []
    for i in range(6):
        row_name = f"abilidade {i+1}"
        if pd.isna(row[row_name]) == True:
            break
        else:
            abilidade.append(row[row_name])
    return abilidade 

if __name__ == '__main__':
    pokedex = PokemonDB("neo4j+s://aa38a78e.databases.neo4j.io", "neo4j", "1camhqRZcZMChJnQG6Y8x5zU1dID5yFbjjEWOXXrLkQ")
    pokemons = pd.read_csv('./dados/pokemons.csv')

    for i, pokemon in pokemons.iterrows():
        id:int = i+1
        name:str = pokemon['pokemon_name']
        peso:float = float(str(pokemon['peso']).split('k')[0].lstrip())
        altura:float = float(str(pokemon['altura']).split('m')[0].lstrip())
        tipo1:str = pokemon['tipo 1']
        tipo2:str = pokemon['tipo 2']
        abilidade:list = get_abilidades(pokemon)

        new_p: Pokemon = Pokemon(id, name, peso, altura, tipo1, tipo2, abilidade)
        pokedex.insert_pokemon(new_p)
    # resp = pokedex.consultar("MATCH (pokemon:POKEMON {id:1}) RETURN pokemon.name")
    # print(resp)
    pokedex.close()