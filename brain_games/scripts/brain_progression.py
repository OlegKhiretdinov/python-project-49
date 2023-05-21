#!/usr/bin/env python3
from brain_games.games.main_wrapper import main_wrapper
from brain_games.games.progression import progression, RULES_DESCRIPTION


def main():
    main_wrapper(RULES_DESCRIPTION, progression)


if __name__ == '__main__':
    main()
