class PokemonDao():
    def __init__(self, instancia__pokemon):
        self.__pokemon_json = {}
        self.preenche_valores_json(instancia__pokemon)

def preenche_valores_json(self, instancia):
    self.__pokemon_json['altura'] = instancia.altura
    self.__pokemon_json['velocidade'] = instancia.velocidade
    self.__pokemon_json['peso'] = instancia.peso
    self.__pokemon_json['ataque'] = instancia.ataque
    self.__pokemon_json['defesa'] = instancia.defesa
    self.__pokemon_json['id'] = instancia.id
    self.__pokemon_json['nome'] = instancia.nome

def __str__(self):
    return str(self.__pokemon_json)

