from random import randint


RULES_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    number = randint(0, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return (correct_answer, number)
