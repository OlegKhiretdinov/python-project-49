#!/usr/bin/env python3
from brain_games.layout.main_layout import main_layout
from brain_games.layout.calc_layout import calc_layout


def main():
    welcome_txt = "What is the result of the expression?"
    main_layout(welcome_txt, calc_layout)


if __name__ == '__main__':
    main()
