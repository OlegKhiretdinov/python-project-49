from random import randint


def prime_layout():
    number = randint(2, 100)
    correct_answer = "yes"
    i = 2

    while i < number:
        if number % i == 0:
            correct_answer = "no"
            break
        i += 1

    return (correct_answer, number)
