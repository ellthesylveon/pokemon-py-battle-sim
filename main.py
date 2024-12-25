import copy
from type_aliases import Pokemon

from create_pokedex import create_pokemon
from pokedex import *
from battle import battle


def main() -> None:

    player_pokemon: Pokemon = copy.deepcopy(MEW)
    opponent_pokemon: Pokemon = copy.deepcopy(PIKACHU)
    player: Pokemon = create_pokemon(player_pokemon)
    opponent: Pokemon = create_pokemon(opponent_pokemon)

    battle(player, opponent)


if __name__ == '__main__':
    main()
