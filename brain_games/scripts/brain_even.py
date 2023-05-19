#!/usr/bin/env python3
from random import randint

from brain_games.cli import welcome_user
from brain_games.utils.utils import (get_answer_for_question,
                                     get_is_answer_correct, finish_game)


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    win_count = 0
    loose_count = 0

    while win_count < 3 and loose_count < 1:
        number = randint(0, 100)
        correct_answer = "yes" if number % 2 == 0 else "no"

        user_answer = get_answer_for_question(number)

        is_answer_correct = get_is_answer_correct(user_answer, correct_answer)

        if is_answer_correct:
            win_count += 1
        else:
            loose_count += 1

    finish_game(win_count == 3, name)


if __name__ == '__main__':
    main()
