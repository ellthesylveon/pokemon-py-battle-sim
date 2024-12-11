import copy
from calculators import calculate_stats

from create_pokedex import create_pokemon
from pokedex import *
from battle import battle


def main() -> None:

    player_pokemon = copy.deepcopy(MEW)
    opponent_pokemon = copy.deepcopy(PIKACHU)
    player = create_pokemon(player_pokemon)
    opponent = create_pokemon(opponent_pokemon)

    battle(player, opponent)


if __name__ == '__main__':
    main()
