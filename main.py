from utils.pokemonDB import PokemonDB
from utils.pokemon import Pokemon
import pandas as pd

lst_pokemons_branched_evo = [
    "Oddish",
    "Poliwag",
    "Slowpoke",
    "Scyther",
    "Eevee",
    "Tyrogue",
    "Wumple",
    "Ralts",
    "Nicada",
    "Snorunt",
    "Clamperl",
    "Burmy",
    "Cosmog",
    "Applin",
    "Charcadet"  
]

def get_abilidades(row: pd.Series) -> list[str]:
    abilidade:list = []
    for i in range(6):
        row_name = f"abilidade {i+1}"
        if pd.isna(row[row_name]) == True:
            break
        else:
            abilidade.append(row[row_name])
    return abilidade 

def get_evolutions(row: pd.Series) -> list[int]:
    evolucao:list = []

    for i in range(9):
        row_name = f"evolucao {i+1}"
        if pd.isna(row[row_name]) == True:
            break
        else:
            evo_id = int(str(row[row_name]).split('-')[0].replace('#',''))
            if evo_id != row['pokemon_id']: evolucao.append(evo_id) 
    return evolucao 

def criar_pokemons(i:int, pokemon: pd.Series):
    id:int = i+1
    name:str = pokemon['pokemon_name']
    peso:float = float(str(pokemon['peso']).split('k')[0].lstrip())
    altura:float = float(str(pokemon['altura']).split('m')[0].lstrip())
    tipo1:str = pokemon['tipo 1']
    tipo2:str = pokemon['tipo 2']
    abilidade:list = get_abilidades(pokemon)

    new_p: Pokemon = Pokemon(id, name, peso, altura, tipo1, tipo2, abilidade)
    pokedex.insert_pokemon(new_p)

if __name__ == '__main__':
    pokedex = PokemonDB("neo4j+s://aa38a78e.databases.neo4j.io", "neo4j", "1camhqRZcZMChJnQG6Y8x5zU1dID5yFbjjEWOXXrLkQ")
    pokemons = pd.read_csv('./dados/pokemons.csv')

    print(pokemons.loc[pd.isna(pokemons['evolucao 4']) == False])

    # for i, pokemon in pokemons.iterrows():
    #     # Adiciona os pokemons ao banco, criar um nó para cada pokemon
    #     # criar_pokemons(i, pokemon)

    #     # Vaz a relação de evolução entre os pokemons
    #     print(get_evolutions(pokemon))
    #     break
        


    # resp = pokedex.consultar("MATCH (pokemon:POKEMON {id:1}) RETURN pokemon.name")
    # print(resp)
    pokedex.close()