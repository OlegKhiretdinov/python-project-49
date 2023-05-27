from random import randint


RULES_DESCRIPTION = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def get_round_data():
    number = randint(2, 100)
    correct_answer = "yes" if is_prime(number) else "no"

    return (correct_answer, number)
