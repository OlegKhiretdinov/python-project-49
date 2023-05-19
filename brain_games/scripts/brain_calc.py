#!/usr/bin/env python3
from random import randint, choice

from brain_games.cli import welcome_user
from brain_games.utils.utils import (get_answer_for_question,
                                     get_is_answer_correct, finish_game)


def get_correct_answer(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2


def main():
    name = welcome_user()
    print("What is the result of the expression?")

    operators = ["+", "-", "*"]
    win_count = 0
    loose_count = 0

    while win_count < 3 and loose_count < 1:
        number1 = randint(0, 10)
        number2 = randint(0, 10)
        operator = choice(operators)

        correct_answer = get_correct_answer(number1, number2, operator)
        user_answer = get_answer_for_question(f'{number1} {operator} {number2}')
        is_correct = get_is_answer_correct(user_answer, str(correct_answer))

        if is_correct:
            win_count += 1
        else:
            loose_count += 1

    finish_game(win_count == 3, name)


if __name__ == '__main__':
    main()
