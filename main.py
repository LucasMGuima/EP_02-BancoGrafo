from utils.pokemonDB import PokemonDB
from utils.pokemon import Pokemon
import pandas as pd

lst_pokemons_branched_evo = [
    "Gloom",
    "Poliwhirl",
    "Slowpoke",
    "Scyther",
    "Eevee",
    "Tyrogue",
    "Wumple",
    "Kirila",
    "Nicada",
    "Snorunt",
    "Clamperl",
    "Burmy",
    "Cosmoem",
    "Applin",
    "Charcadet",
    "Mr. Mime"
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
            evo_name = str(row[row_name]).split('-')[1]
            if (evo_name in lst_pokemons_branched_evo):
                # Branched Evo
                if int(row['pokemon_id']) < evo_id: return evo_id
                if int(row["pokemon_id"]) == 44: return list((45, 182))
                if int(row['pokemon_id']) == 61: return list((62, 186))
                if int(row['pokemon_id']) == 79: return list((80, 199))
                if int(row['pokemon_id']) == 123: return list((212, 900))
                if int(row['pokemon_id']) == 133: return list((134, 135, 136, 196, 197, 470, 471, 700))
                if int(row["pokemon_id"]) == 236: return list((106, 107, 237))
                if int(row['pokemon_id']) == 256: return list((266, 268))
                if int(row['pokemon_id']) == 281: return list((282, 475))
                if int(row['pokemon_id']) == 290: return list((291, 292))
                if int(row['pokemon_id']) == 361: return list((362, 478))
                if int(row["pokemon_id"]) == 366: return list((367, 368))
                if int(row['pokemon_id']) == 412: return list((414, 413))
                if int(row["pokemon_id"]) == 790: return list((791, 792))
                if int(row['pokemon_id']) == 840: return list((841, 842, 1011))
                if int(row["pokemon_id"]) == 935: return list((936, 937))
            if (evo_id == int(row['pokemon_id'])+1): return evo_id
            if (pd.isna(row["evolucao 3"]) == True):
                # So tem uma evolucao
                if evo_name != row['pokemon_name']: return evo_id
    return None

def criar_pokemons(i:int, pokemon: pd.Series):
    id:int = int(pokemon['pokemon_id'])
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

    for i, pokemon in pokemons.iterrows():
        # Adiciona os pokemons ao banco, criar um nó para cada pokemon
        criar_pokemons(i, pokemon)
        
    for i, pokemon in pokemons.iterrows():
        # Vaz a relação de evolução entre os pokemons
        lst_evo = get_evolutions(pokemon)
        if(type(lst_evo) is list):
            for evo in lst_evo:
                pokedex.insert_evolution(pokemon['pokemon_id'], evo)
        else:
            if(type(lst_evo) is int): pokedex.insert_evolution(pokemon['pokemon_id'], lst_evo)

    # print(pokedex.consultar("MATCH (b:POKEMON)-[:EVOLUCAO]->(:POKEMON) RETURN b.name;"))

    pokedex.close()