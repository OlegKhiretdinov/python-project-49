from random import randint


def gcd_layout():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = None

    start = number1 if number1 < number2 else number2

    while not correct_answer:
        if number1 % start == 0 and number2 % start == 0:
            correct_answer = start
        else:
            start -= 1

    return (correct_answer, f'{number1} {number2}')
