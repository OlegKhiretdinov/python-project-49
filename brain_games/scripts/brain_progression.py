#!/usr/bin/env python3
from brain_games.layout.main_layout import main_layout
from brain_games.layout.progression_layout import progression_layout


def main():
    welcome_txt = "What number is missing in the progression?"
    main_layout(welcome_txt, progression_layout)


if __name__ == '__main__':
    main()
