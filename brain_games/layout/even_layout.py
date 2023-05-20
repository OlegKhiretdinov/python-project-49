from random import randint


def even_layout():
    number = randint(0, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return (correct_answer, number)
