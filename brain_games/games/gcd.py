from random import randint


RULES_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(number_1, number_2):
    correct_answer = None
    start = number_1 if number_1 < number_2 else number_2

    while not correct_answer:
        if number_1 % start == 0 and number_2 % start == 0:
            correct_answer = start
        else:
            start -= 1
    return correct_answer


def get_round_data():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)

    return (get_gcd(number_1, number_2), f'{number_1} {number_2}')
