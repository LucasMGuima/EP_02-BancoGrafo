from neo4j import GraphDatabase
from utils.pokemon import Pokemon

class PokemonDB:
    def __init__(self, uri, user, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def insert_pokemon(self, pokemon: Pokemon):
        with self.driver.session() as session:
            resp = session.execute_write(self._create_pokemon, pokemon)
            print(resp)

    def consultar(self, query:str):
        with self.driver.session() as session:
            resp = list(session.run(query))
            return resp

    @staticmethod
    def _create_pokemon(tx, pokemon: Pokemon):
        dados_pokemon = "{{{{id:{id}, name:'{name}', peso:{peso}, altura:{altura}, tipo1:'{tipo1}', tipo2:'{tipo2}', abilidade:{abilidade}}}}}".format(name=pokemon.name.replace('\'', '_'), id=pokemon.id, peso=pokemon.peso, altura=pokemon.altura, tipo1=pokemon.tipo1, tipo2=pokemon.tipo2, abilidade=pokemon.abilidade)
        dados_pokemon = dados_pokemon[1:-1]
        query:str = f"CREATE (`{pokemon.name}`:POKEMON {dados_pokemon})"
        print(query)
        result = tx.run(query)
        return result