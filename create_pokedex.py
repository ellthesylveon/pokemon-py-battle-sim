import csv

from moves import *

def create_pokedex() -> list[dict[str, str | int]]:
    pokedex = []

    print("Loading pokedex data...")
    file = open("pokedex.csv", "r")
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

        pokedex.append(dex_entry)

    file.close()

    print("Pokedex successfully loaded.")
    return pokedex

def create_pokemon(pokemon: dict[str, str | int | list[str | int]]) -> dict[str, str | int | list]:
    evs:list[int] = []
    ivs: list[int] = []
    moves: list[dict[str, str | int | list[str]]] = [POUND, PROTECT, PSYCHIC, EARTHQUAKE]
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

    return pokemon
