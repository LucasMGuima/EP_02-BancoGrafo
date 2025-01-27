from neo4j import GraphDatabase
from utils.pokemon import Pokemon

class PokemonDB:
    def __init__(self, uri, user, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def insert_pokemon(self, pokemon: Pokemon):
        with self.driver.session() as session:
            session.execute_write(self._create_pokemon, pokemon)
            
    def insert_evolution(self, pokemon: str, evo_to: str):
        if not evo_to: return
        with self.driver.session() as session:
            session.execute_write(self._create_evolution, pokemon, evo_to)

    def consultar(self, query:str):
        with self.driver.session() as session:
            resp = list(session.run(query))
            return resp

    @staticmethod
    def _create_pokemon(tx, pokemon: Pokemon):
        dados_pokemon = "{{{{id:{id}, name:'{name}', peso:{peso}, altura:{altura}, tipo1:'{tipo1}', tipo2:'{tipo2}', abilidade:{abilidade}}}}}".format(name=pokemon.name.replace('\'', '_'), id=pokemon.id, peso=pokemon.peso, altura=pokemon.altura, tipo1=pokemon.tipo1, tipo2=pokemon.tipo2, abilidade=pokemon.abilidade)
        dados_pokemon = dados_pokemon[1:-1]
        query:str = f"CREATE (id{pokemon.id}:POKEMON {dados_pokemon})"
        tx.run(query)
    
    @staticmethod
    def _create_evolution(tx, pokemom: str, evolucao: str):
        query:str = "MATCH (p:POKEMON {op}id:{pokemon}{ed}), (e:POKEMON {op}id:{evolucao}{ed}) CREATE (p)-[_{pokemon}to_{evolucao}:EVOLUCAO]->(e)".format(pokemon=pokemom, evolucao=evolucao, op="{", ed="}")
        tx.run(query)
