import math as mt
import random
from type_aliases import Pokemon


def damage_calc(rel_atk: int, rel_def: int, level: int, power: int | float, damage_modifier: float) -> int:
    damage: int = round(((((((2 * level) / 5) + 2) * power * (rel_atk / rel_def)) / 50) + 2) *
                        (random.randint(85, 100) / 100))

    damage *= damage_modifier

    return damage


def calculate_stats(pokemon: Pokemon) -> Pokemon:
    temp_base = [pokemon['base_hp'], pokemon['base_atk'], pokemon['base_def'], pokemon['base_spatk'], pokemon['base_spdef'], pokemon['base_spe']]
    hp_stat: int = 1 if pokemon['name'] == 'Shedinja' else mt.floor(
        ((2 * pokemon['base_hp'] + pokemon['ivs'][0] + mt.floor(pokemon['evs'][0] / 4)) * pokemon['level'] / 100) + pokemon['level'] + 10)
    pokemon.update({'stats': [int(hp_stat)]})
    temp_base.pop(0)

    i: int = 0
    for stat in temp_base:
        other_stat: int = mt.floor(
            (mt.floor((2 * stat + pokemon['ivs'][i] + mt.floor(pokemon['evs'][i] / 4)) * pokemon['level']) / 100) + 5)
        pokemon['stats'].append(int(other_stat))
        i += 1

    pokemon.update({'current_hp': pokemon['stats'][0]})

    return pokemon