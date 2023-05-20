from random import randint


def progression_layout():
    number = randint(1, 20)
    step = randint(1, 5)
    length = randint(5, 10)
    hidden_element_index = randint(0, length-1)
    index = 0
    question = ""

    while index < length:
        if index == hidden_element_index:
            correct_answer = number
            question += '.. '
        else:
            question += f'{str(number)} '

        number += step
        index += 1

    return (correct_answer, question)
