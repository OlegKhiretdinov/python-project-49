#!/usr/bin/env python3
from brain_games.layout.main_layout import main_layout
from brain_games.layout.prime_layout import prime_layout


def main():
    welcome_txt = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')
    main_layout(welcome_txt, prime_layout)


if __name__ == '__main__':
    main()
