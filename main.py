import math as mt
import random

import statdex
from movedex import *


class Pokemon:
    def __init__(self, name: str, level: int, base_stats: dict[str, int], types: list[str],
                 ability: str, evs: list[int], ivs: list[int], nature: str, hp: int | None,
                 stats: list[int], move_list: list[Move]):
        self.name = name
        self.level = level
        self.base_stats = base_stats
        self.types = types
        self.ability = ability
        self.evs = evs
        self.ivs = ivs
        self.nature = nature
        self.stats = stats
        self.hp = hp
        self.move_list = move_list

    def is_alive(self) -> bool:
        if self.hp > 0:
            return True
        else:
            print(f'{self.name} fainted!')
            return False

    def calculate_stats(self) -> None:
        temp_base = list(self.base_stats.values())
        hp_stat: int = mt.floor(
            ((2 * temp_base[0] + self.ivs[0] + mt.floor(self.evs[0] / 4)) * self.level / 100) + self.level + 10)
        self.stats.append(hp_stat)
        self.hp = hp_stat
        temp_base.pop(0)
        i: int = 0
        for stat in temp_base:
            other_stat: int = mt.floor(
                (mt.floor((2 * stat + self.ivs[i + 1] + mt.floor(self.evs[i + 1] / 4)) * self.level) / 100) + 5)
            self.stats.append(other_stat)
            i += 1

    def attack(self, move: Move, target) -> None:
        print(f'{self.name} used {move.name}!')
        match move.category:
            case 'physical':
                rel_atk, rel_def = self.stats[1], target.stats[2]
            case 'special':
                rel_atk, rel_def = self.stats[3], target.stats[4]
        if move.accuracy < 100 & random.randint(0, 100) > move.accuracy:
            print(f'{self.name}\'s attack missed!')
        else:
            damage = damage_calc(rel_atk, rel_def, self.level, move.power)
            if damage > target.hp: damage = target.hp
            target.hp -= damage
            print(f'The enemy {target.name} lost {round(damage / target.stats[0] * 100)}% of its HP!')


class Calculator:
    def __init__(self, ):
        ...


def battle(player: Pokemon, opponent: Pokemon) -> None:
    player.calculate_stats()
    opponent.calculate_stats()
    while player.is_alive() and opponent.is_alive():
        valid_input = False
        while not valid_input:
            print("Please select a move:")
            move_list = [player.move_list[0].name, player.move_list[1].name, player.move_list[2].name,
                         player.move_list[3].name]
            delimiter = ', '
            move_list_str = delimiter.join(move_list)
            print(move_list_str)
            user_input = input()
            if user_input == '1':
                move, valid_input = player.move_list[0], True
            elif user_input == '2':
                move, valid_input = player.move_list[1], True
            elif user_input == '3':
                move, valid_input = player.move_list[2], True
            elif user_input == '4':
                move, valid_input = player.move_list[3], True
            else:
                print("Invalid choice.")
        player.attack(move, opponent)


def damage_calc(rel_atk: int, rel_def: int, level: int, power: int | float) -> int:
    damage: int = round(
        ((((((2 * level) / 5) + 2) * power * (rel_atk / rel_def)) / 50) + 2) * (random.randint(85, 100) / 100))
    return damage


def move_select(player: Pokemon) -> Move:
    valid_input = False
    while not valid_input:
        print("Please select a move:")
        move_list = [player.move_list[0].name, player.move_list[1].name, player.move_list[2].name,
                     player.move_list[3].name]
        delimiter = ', '
        move_list_str = delimiter.join(move_list)
        print(move_list_str)
        user_input = input()
        if user_input == '1':
            move, valid_input = move_list[0], True
        elif user_input == '2':
            move, valid_input = move_list[1], True
        elif user_input == '3':
            move, valid_input = move_list[2], True
        elif user_input == '4':
            move, valid_input = move_list[3], True
        else:
            print("Invalid choice.")
        return move


def main() -> None:
    player: Pokemon = Pokemon(statdex.mew['name'], 100, statdex.mew['base stats'], statdex.mew['types'],
                              statdex.mew['ability'], statdex.mew['evs'], statdex.mew['ivs'], 'Hardy', None,
                              [], [POUND, MEGA_PUNCH, HYPER_VOICE, BOOMBURST])
    opponent: Pokemon = player
    # opponent.calculate_stats()
    # print(opponent.stats[3])
    # print(opponent.stats)
    battle(player, opponent)


if __name__ == '__main__':
    main()
