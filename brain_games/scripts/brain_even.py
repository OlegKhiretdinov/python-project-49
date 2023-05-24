#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.even import even, RULES_DESCRIPTION


def main():
    engine(RULES_DESCRIPTION, even)


if __name__ == '__main__':
    main()
