#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.prime import prime, RULES_DESCRIPTION


def main():
    engine(RULES_DESCRIPTION, prime)


if __name__ == '__main__':
    main()
