#!/usr/bin/env python3
from random import randint

from brain_games.cli import welcome_user
from brain_games.utils.utils import (get_answer_for_question,
                                     get_is_answer_correct, finish_game)


def get_correct_answer(number1, number2):
    start = number1 if number1 < number2 else number2
    result = None

    while not result:
        if number1 % start == 0 and number2 % start == 0:
            result = start
        else:
            start -= 1

    return result


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    win_count = 0
    loose_count = 0

    while win_count < 3 and loose_count < 1:
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        correct_answer = get_correct_answer(number1, number2)
        user_answer = get_answer_for_question(f'{number1} {number2}')
        is_correct = get_is_answer_correct(user_answer, str(correct_answer))

        if is_correct:
            win_count += 1
        else:
            loose_count += 1

    finish_game(win_count == 3, name)


if __name__ == '__main__':
    main()
