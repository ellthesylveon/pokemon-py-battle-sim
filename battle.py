import copy

from typechart import *
from calculators import *
from moves import *


def is_alive(pokemon: dict[str, str | int | list[str | int | float]]) -> bool:
    if pokemon['current_hp'] > 0:
        return True
    else:
        print(f'{pokemon['name']} fainted!')
        return False


def create_type_chart(pokemon: dict[str, str | int | list[str | int | float]]) -> dict[str, int]:
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
    player_speed: int = round(player['stats'][5] * player['stat_stage'][4])
    opponent_speed: int = round(player['stats'][5] * player['stat_stage'][4])
    turn_counter: int = 0
    trick_room: bool = False

    if player['is_paralyzed']:
        player_speed = round(player_speed / 2)
    if opponent['is_paralyzed']:
        opponent_speed = round(opponent_speed / 2)

    while True:
        valid_input = False
        while not valid_input:
            print('Player 1, please select a move:')
            player1_move_list = [player['moves'][0], player['moves'][1], player['moves'][2],
                         player['moves'][3]]
            # for move in player1_move_list:
            #     delimiter = ', '
            move_list_str = 'Nasty Plot, Swords Dance, Psychic, Earthquake'
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
                print('Invalid choice.')

        valid_input = False
        while not valid_input:
            print('Player 2, please select a move:')
            player2_move_list = [opponent['moves'][0], opponent['moves'][1], opponent['moves'][2],
                                 opponent['moves'][3]]
            # for move in player2_move_list:
            #     delimiter = ', '
            move_list_str = 'Nasty Plot, Swords Dance, Psychic, Earthquake'
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
                print('Invalid choice.')

        if trick_room:
            player_speed = (10_000 - round(player['stats'][5] * player['stat_stage'][4])) - 8192
            opponent_speed = (10_000 - round(opponent['stats'][5] * opponent['stat_stage'][4])) - 8192
        else:
            player_speed: int = round(player['stats'][5] * player['stat_stage'][4])
            opponent_speed: int = round(opponent['stats'][5] * opponent['stat_stage'][4])

        if player_speed == opponent_speed and player1_move['priority'] == player2_move['priority']:
            coin_flip = random.randint(0, 1)
            match coin_flip:
                case 0:
                    if not paralysis_check(player):
                        attack(player, player1_move, opponent, turn_counter)
                        if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                            break
                        attack(opponent, player2_move, player, turn_counter)
                        if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                            break
                case 1:
                    if not paralysis_check(opponent):
                        attack(opponent, player2_move, player, turn_counter)
                    if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                        break
                    attack(player, player1_move, opponent, turn_counter)

        elif player_speed > opponent_speed or player1_move['priority'] > player2_move['priority']:
            if not paralysis_check(player):
                attack(player, player1_move, opponent, turn_counter)
                if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                    break
            if not paralysis_check(opponent):
                attack(opponent, player2_move, player, turn_counter)
                if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                    break

        else:
            if not paralysis_check(opponent):
                attack(opponent, player2_move, player, turn_counter)
                if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                    break
            if not paralysis_check(player):
                attack(player, player1_move, opponent, turn_counter)
                if player['current_hp'] == 0 or opponent['current_hp'] == 0:
                    break


def attack(pokemon: dict[str, str | int | list[str | int | float] | dict[str, bool]], move: dict[str, str | int | dict[str, bool] | None], target: dict[str, str | int | list[str|int]], turn_counter: int) -> None:

    target_max_hp = target['stats'][0]

    print(f'{pokemon['name']} used {move['name']}!')

    if 'stat_boost' in move['flags']:
        pokemon['stat_stage'][0] += move['boost_amount'][0]
        pokemon['stat_stage'][1] += move['boost_amount'][1]
        pokemon['stat_stage'][2] += move['boost_amount'][2]
        pokemon['stat_stage'][3] += move['boost_amount'][3]
        pokemon['stat_stage'][4] += move['boost_amount'][4]
        target['stat_stage'][0] -= move['boost_amount'][0]
        target['stat_stage'][1] -= move['boost_amount'][1]
        target['stat_stage'][2] -= move['boost_amount'][2]
        target['stat_stage'][4] -= move['boost_amount'][3]
        target['stat_stage'][4] -= move['boost_amount'][4]
        print(f'{pokemon['name']}\'s {move['boost_category']}')
    
    match move['category']:
        case 'physical':
            rel_atk, rel_def = pokemon['stats'][1] * pokemon['stat_stage'][0], target['stats'][2] * target['stat_stage'][1]
        case 'special':
            rel_atk, rel_def = pokemon['stats'][3] * pokemon['stat_stage'][2], target['stats'][4] * target['stat_stage'][4]
        case 'status':
            rel_atk, rel_def = 0, 1

    if 'protects' in move['flags']:
        pokemon.update({'is_protected': True})
    elif move['accuracy'] < 100 and random.randint(0, 100) > move['accuracy']:
        print(f'{pokemon['name']}\'s attack missed!')
    else:
        damage_modifier: float = 1.0
        # Apply STAB modifier
        if move['type_'] in pokemon['type_']:
            damage_modifier *= 1.5
        # Apply Strength/Resistance modifier
        target_type_chart = create_type_chart(target)
        type_effectiveness = target_type_chart[move['type_']]
        if target['is_protected'] and 'breaks_protect' not in move['flags']:
            print(f'{target['name']} protected itself!')
            damage_modifier = 0
        if 'paralysis' in move['flags'] and damage_modifier != 0:
            if not target['paralysis_immune'] and not target['is_protected']:
                target.update({'is_paralyzed': True})
                print(f'{target['name']} is paralyzed! It may be unable to move.')
            else:
                print(f'{target['name']} can\'t be paralyzed...')
        else:
            if type_effectiveness > 1:
                print('It\'s super effective!')
            elif type_effectiveness == 0:
                print(f'{target['name']} is unaffected...')
                return
            elif type_effectiveness < 1:
                print('It\'s not very effective...')

            damage_modifier *= type_effectiveness

        if move['category'] == 'status':
            damage = 0
        else:
            damage = round(damage_calc(rel_atk, rel_def, pokemon['level'], move['power'], damage_modifier))
            if damage > target_max_hp and target['current_hp'] == target_max_hp:
                damage = target_max_hp
                print(f'{target['name']} lost 100% of its HP!')
            elif damage > target['current_hp']:
                damage = target['current_hp']
                print(f'{target['name']} lost {round(damage / target_max_hp * 100)}% of its HP!')
            else:
                print(f'{target['name']} lost {round(damage / target_max_hp * 100)}% of its HP!')

        target['current_hp'] -= damage

    if target['is_protected']:
        target.update({'is_protected': False})

def paralysis_check(pokemon: dict[str, str | int | list[str | int | float] | dict[str, bool]]) -> bool:
    if pokemon['is_paralyzed'] and random.randint(1, 100) < 26:
        print(f'{pokemon['name']}\'s fully paralyzed!')
        return True
    else:
        return False