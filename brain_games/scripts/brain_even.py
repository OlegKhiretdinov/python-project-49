#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    win_count = 0
    loose_count = 0

    while win_count < 3 and loose_count < 1:
        number = randint(0, 100)
        correct_answer = "yes" if number % 2 == 0 else "no"

        print(f'Question: {number}')
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            win_count += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            loose_count += 1

    if loose_count == 1:
        print(f'Let\'s try again, {name}!')
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
