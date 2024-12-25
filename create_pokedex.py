import csv
import os

from moves import *
from type_aliases import Pokemon


path_to_this_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(path_to_this_directory, 'pokedex.csv')

def create_pokedex() -> list[dict[str, str | int | dict[str, bool]]]:
    pokedex = []

    print('Loading pokedex data...')
    file = open(csv_path, 'r')
    reader = csv.reader(file)
    for line in reader:
        dex_entry = {
            'name': line[0],
            'form': line[1],
            'type_': [line[2]],
            'base_hp': int(line[4]),
            'base_atk': int(line[5]),
            'base_def': int(line[6]),
            'base_spatk': int(line[7]),
            'base_spdef': int(line[8]),
            'base_spe': int(line[9])
        }

        if len(line[3]) > 0:
            dex_entry['type_'].append(line[3])

        if 'electric' in dex_entry['type_']:
            dex_entry.update({'paralysis_immune': True})
        else:
            dex_entry.update({'paralysis_immune': False})

        pokedex.append(dex_entry)

    file.close()

    print('Pokedex successfully loaded.')
    return pokedex


def create_pokemon(pokemon: Pokemon) -> Pokemon:
    evs:list[int] = []
    ivs: list[int] = []
    moves: list[dict[str, str | int | list[str]]] = [NASTY_PLOT, PROTECT, PSYCHIC, EARTHQUAKE]
    while len(ivs) < 6:
        user_input = input('Please enter your pokemon\'s IVs in order of HP, Atk, Def, SpAtk, SpDef, Spe. Leave blank for all 31s. ')
        if user_input == '':
            ivs = [31, 31, 31, 31, 31, 31]
        else:
            ivs.append(int(user_input))

    while len(evs) < 6:
        user_input = input('Please enter your pokemon\'s EVs in the order of HP, Atk, Def, SpAtk, SpDef, Spe. ')
        if user_input == '':
            evs.append(0)
        else:
            evs.append(int(user_input))

    pokemon.update({'ivs': ivs})
    pokemon.update({'evs': evs})
    pokemon.update({'level': 100})
    pokemon.update({'moves': moves})
    pokemon.update({'is_protected': False})
    pokemon.update({'is_paralyzed': False})
    pokemon.update({'is_burned': False})
    pokemon.update({'is_statused': False})
    pokemon.update({'is_confused': False})
    pokemon.update({'stat_stage': [1.0, 1.0, 1.0, 1.0, 1.0]}) # [atk, def, sp.atk, sp.def, spe]
    pokemon.update({'protected_turns': 0})

    return pokemon
