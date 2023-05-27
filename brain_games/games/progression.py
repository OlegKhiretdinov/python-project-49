from random import randint


RULES_DESCRIPTION = "What number is missing in the progression?"


def calculate_progression(initial, difference, length):
    progression = [initial]
    i = 1

    while i < length:
        progression.append(progression[i - 1] + difference)
        i += 1

    return progression


def hide_progression_element(progression, index):
    hidden_element = progression.pop(index)
    progression.insert(index, "..")

    return hidden_element


def get_round_data():
    initial = randint(1, 20)
    difference = randint(1, 5)
    length = randint(5, 10)
    hidden_element_index = randint(0, length - 1)

    progression = calculate_progression(initial, difference, length)
    hidden_item = hide_progression_element(progression, hidden_element_index)

    return (hidden_item, " ".join(str(item) for item in progression))
