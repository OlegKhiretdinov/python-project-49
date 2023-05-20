#!/usr/bin/env python3
from brain_games.layout.main_layout import main_layout
from brain_games.layout.even_layout import even_layout


def main():
    welcome_txt = 'Answer "yes" if the number is even, otherwise answer "no".'
    main_layout(welcome_txt, even_layout)


if __name__ == '__main__':
    main()
