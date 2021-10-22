from src.classes.pokemon import Pokemon
from src.dao.pokemon_dao import PokemonDao
from src.bd.bc_connection import bd 

pokemon1 = Pokemon("fogo voador", "Charizard", 1.7, 90.5, 50, 50, 60 )
nova_dao = PokemonDao(pokemon1)
bd.insert_in_BD(nova_dao._pokemon_json)

pokemon2 = Pokemon("normal", "Eevee", 0.3, 6.5, 40, 30, 40 )
nova_dao2 = PokemonDao(pokemon2)
bd.insert_in_BD(nova_dao2._pokemon_json)

pokemon3 = Pokemon("planta", "Bulbasaur", 0.7, 6.9, 30, 30, 30 )
nova_dao3 = PokemonDao(pokemon3)
bd.insert_in_BD(nova_dao3._pokemon_json)

pokemon4 = Pokemon("elétrico", "Pikachu", 0.4, 6.0, 40, 30, 60 )
nova_dao4 = PokemonDao(pokemon4)
bd.insert_in_BD(nova_dao4._pokemon_json)

pokemon5 = Pokemon("fantasma", "Gengar", 1.5, 40.5, 40, 40, 70 )
nova_dao5 = PokemonDao(pokemon5)
bd.insert_in_BD(nova_dao5._pokemon_json)


