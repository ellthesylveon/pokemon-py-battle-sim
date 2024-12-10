import copy

from create_pokedex import create_pokemon
from pokedex import *
from battle import battle


def main() -> None:

    player_pokemon = copy.deepcopy(MEW)
    opponent_pokemon = copy.deepcopy(MEW)
    player = create_pokemon(player_pokemon)
    opponent = create_pokemon(opponent_pokemon)

    battle(player, opponent)


if __name__ == '__main__':
    main()
