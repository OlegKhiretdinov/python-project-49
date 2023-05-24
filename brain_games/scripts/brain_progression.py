#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.progression import progression, RULES_DESCRIPTION


def main():
    engine(RULES_DESCRIPTION, progression)


if __name__ == '__main__':
    main()
