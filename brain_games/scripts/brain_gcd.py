#!/usr/bin/env python3
from brain_games.layout.main_layout import main_layout
from brain_games.layout.gcd_layout import gcd_layout


def main():
    welcome_txt = 'Find the greatest common divisor of given numbers.'
    main_layout(welcome_txt, gcd_layout)


if __name__ == '__main__':
    main()
