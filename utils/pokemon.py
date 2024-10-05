class Pokemon:
    def __init__(self, id: int, name: str, peso: float, altura: float, tipo1: str, tipo2: str, abilidade: list[str]):
        """
            Novo pokemon.
            
            Keyword arguments:\n
            id -- id da pokedex\n
            name -- nome do pokemon\n
            peso -- peso do pokemon (Kg)\n
            altura -- altrua do pokemon (m)\n
            tipo1 -- tipo primario do pokemon\n
            tipo2 -- tipo secundario do pokemon\n
            abilidade -- lista do nome das abilidades do pokemon\n
        """
        self.id = id
        self.name = name
        self.peso = peso
        self.altura = altura
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.abilidade = abilidade