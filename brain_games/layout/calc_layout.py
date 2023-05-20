from random import randint, choice


def calc_layout():
    operators = ["+", "-", "*"]
    number1 = randint(0, 10)
    number2 = randint(0, 10)
    operator = choice(operators)

    match operator:
        case "+":
            correct_answer = number1 + number2
        case "-":
            correct_answer = number1 - number2
        case "*":
            correct_answer = number1 * number2

    return (correct_answer, f'{number1} {operator} {number2}')
