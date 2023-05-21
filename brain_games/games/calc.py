from random import randint, choice


RULES_DESCRIPTION = "What is the result of the expression?"


def calc():
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
