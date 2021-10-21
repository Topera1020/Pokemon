class PokemonDao():
    def __init__(self, instancia__pokemon):
        self._pokemon_json = {}
        self.preenche_valores_json(instancia__pokemon)

    def preenche_valores_json(self, instancia):
        self._pokemon_json['id'] = instancia.id
        self._pokemon_json['nome'] = instancia.nome
        self._pokemon_json['altura'] = instancia.altura
        self._pokemon_json['peso'] = instancia.peso
        self._pokemon_json['ataque'] = instancia.ataque
        self._pokemon_json['defesa'] = instancia.defesa
        self._pokemon_json['velocidade'] = instancia.velocidade

    def __str__(self):
     return str(self._pokemon_json)

