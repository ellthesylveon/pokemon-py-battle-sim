import copy

from typechart import *
from calculators import *
from moves import *


def is_alive(pokemon: dict[str, str | int | list[str|int]]) -> bool:
    if pokemon['current_hp'] > 0:
        return True
    else:
        print(f'{pokemon['name']} fainted!')
        return False


def create_type_chart(pokemon: dict[str, str | int | list[str|int]]) -> dict[str, int]:
    type_chart = copy.deepcopy(expanded_type_chart[pokemon['type_'][0]])
    if len(pokemon['type_']) > 1:
        second_type_chart = expanded_type_chart[pokemon['type_'][1]]
        for t in type_list:
            type_chart[t] *= second_type_chart[t]

    # Here abilities should be factored into the type chart but we can implement that later

    return type_chart


def battle(player: dict[str, str | int | list[str | int]], opponent: dict[str, str | int | list[str|int]]) -> None:
    calculate_stats(player)
    calculate_stats(opponent)
    player_current_hp: int = player['current_hp']
    opponent_current_hp: int = opponent['current_hp']
    player_speed: int = player['stats'][5]
    opponent_speed: int = opponent['stats'][5]
    turn_counter: int = 0

    while player_current_hp > 0 and opponent_current_hp > 0:
        valid_input = False
        while not valid_input:
            print("Player 1, please select a move:")
            player1_move_list = [player['moves'][0], player['moves'][1], player['moves'][2],
                         player['moves'][3]]
            for move in player1_move_list:
                delimiter = ', '
                move_list_str = 'Feint, Protect, Psychic, Earthquake'
            print(move_list_str)
            user_input = input()
            if user_input == '1':
                player1_move, valid_input = player['moves'][0], True
            elif user_input == '2':
                player1_move, valid_input = player['moves'][1], True
            elif user_input == '3':
                player1_move, valid_input = player['moves'][2], True
            elif user_input == '4':
                player1_move, valid_input = player['moves'][3], True
            else:
                print("Invalid choice.")

        valid_input = False
        while not valid_input:
            print("Player 2, please select a move:")
            player2_move_list = [opponent['moves'][0], opponent['moves'][1], opponent['moves'][2],
                                 opponent['moves'][3]]
            for move in player2_move_list:
                delimiter = ', '
                move_list_str = 'Feint, Protect, Psychic, Earthquake'
            print(move_list_str)
            user_input = input()
            if user_input == '1':
                player2_move, valid_input = player['moves'][0], True
            elif user_input == '2':
                player2_move, valid_input = player['moves'][1], True
            elif user_input == '3':
                player2_move, valid_input = player['moves'][2], True
            elif user_input == '4':
                player2_move, valid_input = player['moves'][3], True
            else:
                print("Invalid choice.")

        if player_speed == opponent_speed & player1_move['priority'] == player2_move['priority']:
            coin_flip = random.randint(0, 1)
            match coin_flip:
                case 0:
                    attack(player, player1_move, opponent, turn_counter)
                case 1:
                    attack(opponent, player2_move, player, turn_counter)
        elif player_speed > opponent_speed or player1_move['priority'] > player2_move['priority']:
            attack(player, player1_move, opponent, turn_counter)
            attack(opponent, player2_move, player, turn_counter)
        else:
            attack(opponent, player2_move, player, turn_counter)
            attack(player, player1_move, opponent, turn_counter)


def attack(pokemon: dict[str, str | int | list[str|int]], move: dict[str, str | int | dict[str, bool] | None], target: dict[str, str | int | list[str|int]], turn_counter: int) -> None:

    target_max_hp = target['stats'][0]
    target_current_hp = target['current_hp']


    print(f'{pokemon['name']} used {move['name']}!')
    match move['category']:
        case 'physical':
            rel_atk, rel_def = pokemon['stats'][1], target['stats'][2]
        case 'special':
            rel_atk, rel_def = pokemon['stats'][3], target['stats'][4]
        case 'status':
            pass
    if move == PROTECT:
        pokemon.update({'is_protected': True})
    elif move['accuracy'] < 100 & random.randint(0, 100) > move['accuracy']:
        print(f'{pokemon['name']}\'s attack missed!')
    else:
        damage_modifier: float = 1
        if target['is_protected']:
            if 'breaks_protect' not in move['flags']:
                print(f'The enemy {target['name']} protected itself!')
                damage_modifier = 0
        else:
            # Apply STAB modifier
            if move['type_'] in pokemon['type_']:
                damage_modifier *= 1.5
            # Apply Strength/Resistance modifier
            target_type_chart = create_type_chart(target)
            type_effectiveness = target_type_chart[move['type_']]
            if type_effectiveness > 1:
                print("It's super effective!")
            elif type_effectiveness == 0:
                print(f'The enemy {target['name']} is unaffected...')
                return
            elif type_effectiveness < 1:
                print("It's not very effective...")

            damage_modifier *= type_effectiveness

        damage = damage_calc(rel_atk, rel_def, pokemon['level'], move['power'], damage_modifier)

        if damage > target_max_hp & target_current_hp == target_max_hp:
            damage = target_max_hp
            print(f'The enemy {target['name']} lost 100% of its HP!')
        else:
            print(f'The enemy {target['name']} lost {round(damage / target_max_hp * 100)}% of its HP!')

        target_current_hp -= damage
        target.update({'current_hp': round(target_current_hp)})

        if target['is_protected']:
            target.update({'is_protected': False})