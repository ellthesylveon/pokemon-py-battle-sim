import copy

from create_pokedex import create_pokemon
from pokedex import *
from battle import battle



# def create_pokemon(dex_entry):
#     hp_stat: int = mt.floor(
#         ((2 * temp_base[0] + dex_entry.ivs[0] + mt.floor(dex_entry.evs[0] / 4)) * dex_entry.level / 100) + dex_entry.level + 10)
#     dex_entry.stats.append(hp_stat)
#     dex.hp = hp_stat
#     temp_base.pop(0)
#     i: int = 0
#     for stat in temp_base:
#         other_stat: int = mt.floor(
#             (mt.floor((2 * stat + pokemon.ivs[i + 1] + mt.floor(pokemon.evs[i + 1] / 4)) * pokemon.level) / 100) + 5)
#         pokemon.stats.append(other_stat)
#         i += 1


def main() -> None:

    player_pokemon = copy.deepcopy(MEW)
    opponent_pokemon = copy.deepcopy(MEW)
    player = create_pokemon(player_pokemon)
    opponent = create_pokemon(opponent_pokemon)

    

    battle(player, opponent)


if __name__ == '__main__':
    main()
