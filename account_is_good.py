#!/usr/bin/env python
# -*- coding: utf-8 -*-
import secrets


def number_to_have():
    """
    Generate a random value between 101 and 999.

    :return: An integer between 101 and 999.
    """
    return secrets.randbelow(999 - 101 + 1) + 101


def tiles():
    """
    Generate tiles and takes 6 on 24 tiles available.

    :return: 6 tiles in the array
    """
    present_tiles = list(range(1, 11)) * 2 + [25, 50, 75, 100]
    take_tiles = []

    for _ in range(6):
        index = secrets.randbelow(len(present_tiles))
        take_tiles.append(present_tiles[index])
        present_tiles.pop(index)

    return take_tiles


def apply_operation(operator, number1, number2):
    """
    Apply an operation to 2 numbers.

    :param operator: A character
    :param number1: First value
    :param number2: Second value
    :return: Calculate the value or None if it isn't an operator
    """
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case '/':
            return number1 / number2
        case _:
            print("Le saisie de l'opérateur n'est pas bon. Recommencer")
            return None


def verify_input_user_numbers(input_user, tab_tiles):
    """
    Check whether the numbers entered by the user are in the tiles array.

    :param input_user: Entry user on numbers
    :param tab_tiles: Tiles available array
    :return: A boolean
    """
    tab_values_user = input_user.split()

    if len(tab_values_user) == 2:
        number1, number2 = map(int, tab_values_user)
        if number1 in tab_tiles and number2 in tab_tiles:
            return True

    return False


def continue_game():
    """
    Ask the user if this is the best possible number.

    :return: A boolean
    """
    input_user = ''
    while input_user != 'y' and input_user != 'n':
        input_user = input("Est-ce le nombre le plus proche pour vous ? [y/n]")

    if input_user != 'n':
        print("Le jeu est terminé.")
    return input_user != 'y'


def is_end_game(number_to_account, value, array_size_tiles):
    if value == number_to_account:
        print("Le compte est bon. Félicitations !!!")
        return True

    if array_size_tiles == 1:
        print(f"Le jeu est terminé. Votre nombre est {value}")
        return True

    print(f"Voici le nombre obtenu: {value}")
    return not continue_game()


def loop_game(number_to_account, tab_tiles):
    print(f"Voici le nombre a tomber tout pile: {number_to_account}.")

    while len(tab_tiles) != 1:
        print(f"Voici vos tuiles: {tab_tiles}")
        operator = input("Quelle opérateur souhaites-tu appliquer ? [+,-,*,/] ")
        numbers = input(f"Parmi ces nombres {tab_tiles}, quelles sont les 2 nombres que tu souhaites sélectionner ?")

        if verify_input_user_numbers(numbers, tab_tiles):
            number1, number2 = numbers.split()

            operation_value = apply_operation(operator, int(number1), int(number2))
            if operation_value is not None:
                tab_tiles.remove(int(number1))
                tab_tiles.remove(int(number2))
                tab_tiles.append(operation_value)

                if is_end_game(number_to_account, operation_value, len(tab_tiles)):
                    break


if __name__ == "__main__":
    loop_game(number_to_have(), tiles())
