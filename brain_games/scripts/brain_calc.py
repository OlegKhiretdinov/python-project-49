#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.calc import calc, RULES_DESCRIPTION


def main():
    engine(RULES_DESCRIPTION, calc)


if __name__ == '__main__':
    main()
